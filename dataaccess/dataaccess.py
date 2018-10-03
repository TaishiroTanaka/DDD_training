from db.db import Db


class DataSource:
    @staticmethod
    def get_db():
        return Db
