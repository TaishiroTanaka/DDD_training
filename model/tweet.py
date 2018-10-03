# Valueオブジェクト
class TweetId():
    def __init__(self, tweet_id: int) -> None:
        self.value = tweet_id

    def validate_type(self) -> bool:
        return type(self.value) is int


class Content():
    def __init__(self, content: str) -> None:
        self.value = content

    def validate_type(self) -> bool:
        return type(self.value) is str


class CreateDate():
    def __init__(self, create_date: str) -> None:
        self.value = create_date

    def validate_type(self) -> bool:
        return type(self.value) is str

    def validate_length(self) -> bool:
        return len(self.value) <= 140


class DeleteStatus():
    def __init__(self, delete_status: int) -> None:
        self.value = delete_status

    def validate_type(self) -> bool:
        if self.value == int(0):
            return True
        if self.value == int(1):
            return True

        return False


# エンティティ

class Tweet():
    def __init__(self, tweet_id: TweetId, content: Content,
                 create_date: CreateDate,
                 delete_status: DeleteStatus) -> None:
        self.tweet_id = tweet_id
        self.tweet_content = content
        self.tweet_create_date = create_date
        self.tweet_delete_status = delete_status

    def to_dict(self):
        return {
            'tweet_id': self.tweet_id.value,
            'tweet_content': self.tweet_content.value,
            'tweet_create_date': self.tweet_create_date.value,
            'tweet_delete_status': self.tweet_delete_status.value,
        }
