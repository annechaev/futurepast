import json
import os

from django.db import connection


class FileHelper:

    os_delimiter = "\\" if os.name.lower() != "linux" else "/"

    @classmethod
    def open_json_file(cls, app_name, filename):
        module_dir = os.path.dirname(__file__)
        path = cls.os_delimiter.join([module_dir, app_name, "data", filename])
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)


class DbHelper:

    @staticmethod
    def check_if_table_exists(table_name):
        return table_name in connection.introspection.table_names()
