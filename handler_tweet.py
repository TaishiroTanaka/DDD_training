import json

from dataaccess.tweet import TweetDataSource
from model.tweet_factory import TweetFactory
from service.tweet import TweetCommandService
from service.tweet import TweetQueryService


def register_tweet_handler(params: str) -> str:
    params_dict = json.loads(params)
    tweet = TweetFactory.create(params_dict)

    tweet_datasource = TweetDataSource
    tweet_command_service = TweetCommandService(tweet_datasource)
    result = tweet_command_service.register(tweet)

    if result is True:
        return 'Tweet completed!'
    return 'Tweet failed.'


def find_tweet_handler() -> list:
    tweet_datasource = TweetDataSource
    tweet_query_service = TweetQueryService(tweet_datasource)
    tweet_list = tweet_query_service.find()

    tweet_dict_list = []
    for tweet in tweet_list:
        tweet_dict_list.append(tweet.to_dict())

    return tweet_dict_list
