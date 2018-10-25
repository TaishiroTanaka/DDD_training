import json
from decimal import Decimal

from dataaccess.tweet import TweetDataSource
from model.tweet_factory import TweetFactory
from service.tweet import TweetCommandService
from service.tweet import TweetQueryService


def register_tweet_handler(event, context):
    params = json.loads(event['body'])
    tweet = TweetFactory.create(params)

    tweet_datasource = TweetDataSource()
    tweet_command_service = TweetCommandService(tweet_datasource)
    result = tweet_command_service.register(tweet)

    if result is True:
        body = {
            "message": "Tweet Create Request successfully!",
            "tweet": tweet.to_dict()
        }
        return create_response(200, body)
    else:
        body = {
            "message": "Tweet Create Request failure.",
        }
        return create_response(500, body)


def find_tweet_handler(params: str) -> list:
    params_dict = json.loads(params)

    tweet_datasource = TweetDataSource()
    tweet_query_service = TweetQueryService(tweet_datasource)
    tweet_list = tweet_query_service.find_by_user_id(params_dict['user_id'])

    tweet_dict_list = []
    for tweet in tweet_list:
        tweet_dict_list.append(tweet.to_dict())

    return tweet_dict_list


def create_response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "x-custom-header": "my custom header value"
        },
        "body": json.dumps(body, default=decimal_default_proc)
    }


def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    return obj
