# -*- coding: utf-8 -*-


import json

from dataaccess.dataaccess import DataSource
from model.tweet import Tweet
from util import *


class TweetDataSource():
    def __init__(self) -> None:
        self.datasource = DataSource.get_db()

    def register(self, tweet: Tweet):
        tweet_table_name = get_tweet_table_name()
