from datetime import datetime
import random

from model.tweet import Tweet
from model.tweet import TweetId
from model.tweet import Content
from model.tweet import CreateDate
from model.tweet import UserId

from util import get_timezone


class TweetFactory:
    @staticmethod
    def create(params) -> Tweet:
        tweet_id = random.randint(10000000, 99999999)
        # now_datetime = datetime.now().strftime('%Y/%m/%d')
        now_datetime = datetime.now(get_timezone())

        tweet = Tweet(
            tweet_id=TweetId(tweet_id),
            content=Content(params['content']),
            create_date=CreateDate(now_datetime),
            user_id=UserId(params['user_id'])
        )

        return tweet
