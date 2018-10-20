from model.user import User
from dataaccess.user import UserDataSource


class UserCommandService:
    def __init__(self, user_datasource: UserDataSource) -> None:
        self.user_datasource = user_datasource

    def register(self, user: User) -> bool:
        self.user_datasource.register(user)
        return True

