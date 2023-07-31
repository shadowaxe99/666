```python
import sqlite3
from sqlite3 import Error

class PlatformServices:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def close_connection(self):
        self.connection.close()

    def execute_sql(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
        except Error as e:
            print(e)

    def fetch_data(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(e)

    def update_data(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
        except Error as e:
            print(e)
```