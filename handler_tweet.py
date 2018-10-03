import json

from dataaccess.tweet import TweetDataSource
from model.tweet_factory import TweetFactory
from service.tweet import TweetCommandService


def regist_tweet_handler(params: json):
    params_dict = json.load(params)
    tweet = TweetFactory.create(params_dict)

    tweet_datasource = TweetDataSource
    tweet_command_service = TweetCommandService(tweet_datasource)
    result = tweet_command_service.register(tweet)

    if result is True:
        return 'Tweeted!'
    return 'Tweet failed.'
