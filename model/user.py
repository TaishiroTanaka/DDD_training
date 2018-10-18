class UserId:
    def __init__(self, user_id: int):
        self.value = user_id


class Name:
    def __init__(self, name: str):
        self.value = name


class User:
    def __init__(self, user_id: UserId, name: Name):
        self.user_id = user_id
        self.name = name

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "name": self.name
        }

    def from_dict(self) -> 'User':
        pass