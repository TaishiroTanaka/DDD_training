from model.tweet import Tweet
from dataaccess.tweet import TweetDataSource


class TweetCommandService:
    def __init__(self, tweet_datasource: TweetDataSource) -> None:
        self.tweet_datasource = tweet_datasource

    def register(self, tweet: Tweet) -> bool:
        self.tweet_datasource.register(tweet)
        return True


class TweetQueryService:
    def __init__(self, tweet_datasource: TweetDataSource) -> None:
        self.tweet_datasource = tweet_datasource

    def find(self) -> list:
        return self.tweet_datasource.find()

    def find_by_user_id(self, user_id: str) -> list:
        return self.tweet_datasource.find_by_user_id(user_id)
