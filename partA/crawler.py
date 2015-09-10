#! /usr/bin/env python
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

consumer_key = ""
consumer_secret_key = ""
access_token = ""
access_secret_token = ""

# Keywords
keywords_en = "presidential campaign, #POTUS, "
keywords_ru = "Коммунистическая партия Советского Союза, Дума, Единая Россия, Либерально-демократическая партия России, Владимир Вольфович Жириновский, национализм и популизм, социального консерватизма, Справедливая Россия, социал-демократия, новости, Путин"
keywords_de = ""

# Global Variables
tweet_count_en = 200
tweet_count_ru = 0
tweet_count_de = 200

tweet_list = []

# todo: add all tweets to a single json list

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global tweet_count_ru
        global tweet_list
        if 'text' in data:
            # append incoming tweets to a list
            tweet_list.append(data)
            tweet_count_ru += 1
            print tweet_count_ru

            # when you reach certian number of tweets then just dump the list into a file
            if tweet_count_ru == 200:
                with io.open('tweet_data.txt', 'w', encoding='utf-8') as f:
                    f.write(unicode(json.dumps(tweet_list, ensure_ascii=False)))
                sys.exit()


    def on_error(self, status_code, data):
        print status_code

if __name__ == '__main__':
    
    stream = MyStreamer(consumer_key, consumer_secret_key, access_token, access_secret_token)
    stream.statuses.filter(track=keywords_ru, language="ru")
