import uuid

from model.user import UserId
from model.user import Name
from model.user import User


class UserFactory:
    @staticmethod
    def create(params) -> User:
        user = User(
            user_id=UserId(params['user_id']),
            name=Name(params['name']),
        )

        return user
