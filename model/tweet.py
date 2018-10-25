class TweetId:
    def __init__(self, tweet_id: int) -> None:
        self.value = tweet_id


class Content:
    def __init__(self, content: str) -> None:
        self.value = content


class CreateDate:
    def __init__(self, create_date: str) -> None:
        self.value = create_date


class UserId:
    def __init__(self, user_id: str) -> None:
        self.value = user_id


class Tweet:
    def __init__(self, tweet_id: TweetId,
                 content: Content,
                 create_date: CreateDate,
                 user_id: UserId) -> None:
        self.tweet_id = tweet_id
        self.content = content
        self.create_date = create_date
        self.user_id = user_id

    def to_dict(self):
        return {
            'tweet_id': self.tweet_id.value,
            'content': self.content.value,
            'create_date': self.create_date.value,
            'user_id': self.user_id.value,
        }
               
    @staticmethod
    def from_dict(tweet_dict: dict) -> 'Tweet':
        _dict = tweet_dict.copy()

        return Tweet(
            tweet_id=TweetId(_dict['tweet_id']),
            content=Content(_dict['content']),
            create_date=CreateDate(_dict['create_date']),
            user_id=UserId(_dict['user_id']),
        )
