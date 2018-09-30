# -*- coding: utf-8 -*-


# Valueオブジェクト

class TweetId():
    def __init__(self, tweet_id: int) -> None:
        self.value = tweet_id

    def validate_type(self) -> bool:
        return type(self.value) is int


class TweetContent():
    def __init__(self, tweet_content: str) -> None:
        self.value = tweet_content

    def validate_type(self) -> bool:
        return type(self.value) is str


class TweetCreateDate():
    def __init__(self, tweet_create_date: str) -> None:
        self.value = tweet_create_date

    def validate_type(self) -> bool:
        return type(self.value) is str

    def validate_length(self) -> bool:
        return len(self.value) <= 140


class TweetDeleteStatus():
    def __init__(self, tweet_delete_status: int) -> None:
        self.value = tweet_delete_status

    def validate_type(self) -> bool:
        if self.value == int(0):
            return True
        if self.value == int(1):
            return True

        return False


# エンティティ

class Tweet():
    def __init__(self, tweet_id: TweetId, tweet_content: TweetContent,
                 tweet_create_date: TweetCreateDate,
                 tweet_delete_status: TweetDeleteStatus) -> None:
        self.tweet_id = tweet_id
        self.tweet_content = tweet_content
        self.tweet_create_date = tweet_create_date
        self.tweet_delete_status = tweet_delete_status

    def to_dict(self):
        return {
            'tweet_id': self.tweet_id.value,
            'tweet_content': self.tweet_content.value,
            'tweet_create_date': self.tweet_create_date.value,
            'tweet_delete_status': self.tweet_delete_status.value,
        }
