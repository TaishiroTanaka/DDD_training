from datetime import datetime

import uuid

from model.tweet import Tweet
from model.tweet import TweetId
from model.tweet import Content
from model.tweet import CreateDate
from model.tweet import DeleteStatus


class TweetFactory:
    @staticmethod
    def create(params):
        tweet_id = int(uuid.uuid4().int)
        now_datetime = datetime.now().strftime('%Y/%m/%d')
        delete_status = False

        tweet = Tweet(
            tweet_id=TweetId(tweet_id),
            content=Content(params['content']),
            create_date=CreateDate(now_datetime),
            delete_status=DeleteStatus(delete_status),
        )

        return tweet
