import json


class Table():
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.dir_pass = 'db/' + table_name
        self.file_read = open(self.dir_pass)
        self.data = json.load(self.file_read)

    def put_item(self, new_data: dict):
        data_copy = self.data.copy()
        data_copy.append(new_data)

        file_write = open(self.dir_pass, 'w')
        json.dump(data_copy, file_write, indent=4)

    def scan(self) -> list:
        return self.data
