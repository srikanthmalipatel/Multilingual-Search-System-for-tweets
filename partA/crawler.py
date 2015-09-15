#/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 SrikanthMalipatel <SrikanthMalipatel@Srikanth>
#
# Distributed under terms of the MIT license.

""" 

"""

from twython import Twython
from twython import TwythonStreamer
import json, io
import sys

consumer_key = "Fpsk6Yi6owCPtLjSXaUoZEK7c"
consumer_secret_key = "YezwQhE3Kh3dgXGNVGXUOYhXmTkE38QgmbpToXTc29DZWEnNuF"
access_token = "140017490-REcjx2p6YphicskjJkl61PrHP5hNsYCgdVOoOflP"
access_secret_token = "lHrn7XJiwlnggxFuahDdDkphewnWmIXuvIpE6dAz1NMhj"

# Keywords
keywords_en = "presidential campaign, #POTUS, #obama, #316Political, #feelthebern, #election2016, #presidentionalelection, #bernie_sanders, #republican, #stopirandeal, #conservative"
keywords_ru = "Коммунистическая партия Советского Союза, Дума, Единая Россия, Либерально-демократическая партия России, Владимир Вольфович Жириновский, национализм и популизм, социального консерватизма, Справедливая Россия, социал-демократия, новости, Путин"
keywords_de = "Flüchtlinge, Angela Merkel, Griechenland"

# Global Variables
tweet_count = 0
tweet_list = []
tweet_lang = ["en", "ru", "de"]

# todo: now change the filter and run it after every 200 tweets

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global tweet_count
        global tweet_list
        global stream
        if 'text' in data:
            # append incoming tweets to a list
            tweet_list.append(data)
            tweet_count += 1
            print tweet_count

            # when you reach certian number of tweets then just dump the list into a file
            if tweet_count == 200:
                with io.open('tweet_data_ru_4.txt', 'w', encoding='utf-8') as f:
                    f.write(unicode(json.dumps(tweet_list, ensure_ascii=False)))
                sys.exit()


    def on_error(self, status_code, data):
        print status_code

if __name__ == '__main__':
    stream = MyStreamer(consumer_key, consumer_secret_key, access_token, access_secret_token)
    stream.statuses.filter(track=keywords_ru, language="ru")
