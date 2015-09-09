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

consumer_key = "Fpsk6Yi6owCPtLjSXaUoZEK7c"
consumer_secret_key = "YezwQhE3Kh3dgXGNVGXUOYhXmTkE38QgmbpToXTc29DZWEnNuF"
access_token = "140017490-REcjx2p6YphicskjJkl61PrHP5hNsYCgdVOoOflP"
access_secret_token = "lHrn7XJiwlnggxFuahDdDkphewnWmIXuvIpE6dAz1NMhj"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
        
    def on_error(self, status_code, data):
        print status_code

stream = MyStreamer(consumer_key, consumer_secret_key, access_token, access_secret_token)
stream.statuses.filter(track="lol", language="en")
