import json

from dataaccess.tweet import TweetDataSource
# from model.todo_factory import TodoFactory
from service.tweet import TweetCommonService


def regist_todo_handler(params: json):
    todo = TodoFactory.create(params)

    todo_datasource = TodoDataSource()
    todo_command_service = TodoCommandService(todo_datasource)
    result = todo_command_service.register(todo)
    if result is True:
        body = {
            "message": "Todo Create Request successfully!",
            "todo_id": todo.todo_id.value
        }
        return create_response(200, body)

    else:
        body = {
            "message": "Todo Create Request failure!",
        }
        return create_response(500, body)