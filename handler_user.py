import json
from model.user_factory import UserFactory
from dataaccess.user import UserDataSource
from service.user import UserCommandService


def regist_user_handler(params: str) -> str:
    params_dict = json.loads(params)
    user = UserFactory.create(params_dict)

    user_datasource = UserDataSource
    user_command_service = UserCommandService(user_datasource)
    result = user_command_service.register(user)

    if result is True:
        return 'User registration is completed!'
    return 'User registration failed.'
