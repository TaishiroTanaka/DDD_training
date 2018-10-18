import uuid

from model.user import UserId
from model.user import Name
from model.user import User


class UserFactory:
    @staticmethod
    def create(params):
        user_id = int(uuid.uuid4().int)

        user = User(
            user_id=UserId(user_id),
            name=Name(params['name']),
        )

        return user
