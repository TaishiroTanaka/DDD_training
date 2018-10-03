from model.tweet import Tweet
from util import get_tweet_table_name
from db.db import Table


class TweetDataSource():
    @staticmethod
    def register(tweet: Tweet) -> None:
        tweet_table_name = get_tweet_table_name()
        tweet_table = Table(tweet_table_name)
        tweet_table.put_item(tweet.to_dict())

    @staticmethod
    def find() -> list:
        tweet_table_name = get_tweet_table_name()
        tweet_table = Table(tweet_table_name)
        results = tweet_table.scan()

        tweet_list = []
        for result in results:
            todo = Tweet.from_dict(result)
            tweet_list.append(todo)

        return tweet_list
