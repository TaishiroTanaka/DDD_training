from model.tweet import Tweet
from dataaccess.dataaccess import DataSource
from util import get_tweet_table_name
from db.db import Table


class TweetDataSource:
    def __init__(self):
        self.datasource = DataSource.get_dynamodb()

    def register(self, tweet: Tweet) -> None:
        tweet_table_name = get_tweet_table_name()
        tweet_table = self.datasource.Table(tweet_table_name)
        tweet_dict = DataSource.dynamo_type_encode(tweet.to_dict())
        tweet_table.put_item(Item=tweet_dict)

    def find() -> list:
        tweet_table_name = get_tweet_table_name()
        tweet_table = Table(tweet_table_name)
        results = tweet_table.scan()

        tweet_list = []
        for result in results:
            todo = Tweet.from_dict(result)
            tweet_list.append(todo)

        return tweet_list

    def find_by_user_id(user_id: str) -> list:
        tweet_table_name = get_tweet_table_name()
        tweet_table = Table(tweet_table_name)
        results = tweet_table.scan()

        tweet_list = []
        for result in results:
            if result['user_id'] == user_id:
                tweet = Tweet.from_dict(result)
                tweet_list.append(tweet)

        return tweet_list
