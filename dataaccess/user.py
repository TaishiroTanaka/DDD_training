from model.user import User
from util import get_user_table_name
from db.db import Table


class UserDataSource:
    @staticmethod
    def register(user: User) -> None:
        user_table_name = get_user_table_name()
        user_table = Table(user_table_name)
        user_table.put_item(user.to_dict())
