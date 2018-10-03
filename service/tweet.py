from model.tweet import Tweet
from dataaccess.tweet import TweetDataSource


class TweetCommandService:
    def __init__(self, tweet_datasource: TweetDataSource) -> None:
        self.tweet_datasource = tweet_datasource

    def register(self, tweet: Tweet) -> bool:
        self.tweet = tweet
        self.tweet_datasource.register(self.tweet)
        return True
