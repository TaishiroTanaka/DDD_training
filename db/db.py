import json

from model.tweet import Tweet


# テーブルクラス
class Table():
    def __init__(self, table_name: str):
        dir_pass = 'db/' + table_name
        file = open(dir_pass)
        self.value = json.load(file)

    def put_item(self, tweet: Tweet):
        self.value.update(tweet)


# DBクラス
class Db():
    def __init__(self):
        pass

    def get_table(self):
        pass

    def get_table_all(self):
        pass