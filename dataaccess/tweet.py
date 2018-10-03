import json

from dataaccess.dataaccess import DataSource
from model.tweet import Tweet
from util import *


class TweetDataSource():
    def __init__(self) -> None:
        self.datasource = DataSource.get_db()

    def register(self, tweet: Tweet) -> None:
        tweet_table_name = get_tweet_table_name()
        # tweet_table = self.datasource.Table(todo_table_name)
        # tweet_table.put_item(Tweet)
