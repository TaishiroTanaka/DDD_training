# import json
#
# from dataaccess.dataaccess import DataSource
from model.tweet import Tweet
from util import *
from db.db import Table


class TweetDataSource():
    # def __init__(self) -> None:
    #     self.datasource = DataSource.get_db()

    @staticmethod
    def register(tweet: Tweet) -> None:
        tweet_table_name = get_tweet_table_name()
        tweet_table = Table(tweet_table_name)
        tweet_table.put_item(tweet.to_dict())
