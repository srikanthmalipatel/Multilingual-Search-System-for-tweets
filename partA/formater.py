#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 SrikanthMalipatel <SrikanthMalipatel@Srikanth>
#
# Distributed under terms of the MIT license.

"""

"""

import json, io, pytz
from pytz import timezone
from datetime import datetime

def load(file):
    tweets = []
    for line in file:
        tweets.append(json.loads(line))
    
    count = 0
    ftweets = []
    for tweet in tweets[0]:
        print count
        count += 1
        ftweet = {}
        # set id
        ftweet['id'] = tweet['id_str']
        # created date
        fmt = '%Y-%m-%dT%H:%M:%SZ'
        temp = datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
        ftweet['created_at'] = temp.strftime(fmt)
        # set text fields based on language language
        ftweet['lang'] = tweet['lang']
        if tweet['lang'] == 'en':
            ftweet['text_en'] = tweet['text']
            ftweet['text_ru'] = ""
            ftweet['text_de'] = ""
        elif tweet['lang'] == 'ru':
            ftweet['text_en'] = ""
            ftweet['text_ru'] = tweet['text']
            ftweet['text_de'] = ""
        elif tweet['lang'] == 'de':
            ftweet['text_en'] = ""
            ftweet['text_ru'] = ""
            ftweet['text_de'] = tweet['text']
        # screen name
        ftweet['screen_name'] = tweet['user']['screen_name']
        # user name
        ftweet['user_name'] = tweet['user']['name']
        # location
        ftweet['location'] = tweet['user']['location']
        # tweet hashtag
        ftweet['tweet_hashtag'] = []
        for tag in tweet['entities']['hashtags']:
            ftweet['tweet_hashtag'].append(tag['text'])
        # tweet extended url
        ftweet['tweet_url'] = []
        for url in tweet['entities']['urls']:
            ftweet['tweet_url'].append(url['expanded_url'])
        # append the formated dictionary to ftweets
        ftweets.append(ftweet)


    with io.open('raw_tweet_en.txt', 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(ftweets, ensure_ascii=False)))

if __name__ == '__main__':
    file = open('tweet_data_en_1.txt', 'r')
    load(file)
