import os.path
import sqlite3
import sys
from pprint import pprint


class Db:
    def __init__(self, db_name: str):
        self.__db_name = db_name

    def get_db_name(self) -> str:
        return self.__db_name

    def create_db(self) -> bool:
        try:
            connection = sqlite3.connect(self.get_db_name())
            with open('script_create.sql', 'r') as sql_file:
                sql_script = sql_file.read()

            with connection:
                cursor = connection.cursor()
                cursor.executescript(sql_script)

            return True
        except Exception as e:
            sys.path.remove(self.get_db_name())
            return False

    def does_db_exist(self) -> bool:
        return True if os.path.exists(self.get_db_name()) else False

    def create_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.get_db_name())
        return connection

    def get_all_cities(self) -> dict:
        query = "SELECT * FROM cities"
        rows = self.__get_all_from_db(query)
        return {row[0]: self.__formatted_city(row) for row in rows}

    def get_all_regions(self) -> dict:
        query = "SELECT * FROM regions"
        rows = self.__get_all_from_db(query)
        return {row[0]: self.__formatted_region(row) for row in rows}

    def get_all_users(self) -> dict:
        query = "SELECT * FROM users"
        rows = self.__get_all_from_db(query)
        return {row[0]: self.__formatted_user(row) for row in rows}

    def get_city_by_name(self, name: str) -> dict:
        return self.__get_city_by_filter(f"city_name='{name}'")

    def get_region_by_name(self, name: str) -> dict:
        return self.__get_region_by_filter(f"region_name='{name}'")

    def __get_all_from_db(self, query) -> list:
        connection = self.create_connection()
        result = [row for row in connection.execute(query)]
        return result

    def __get_city_by_filter(self, where: str) -> dict:
        query = f"SELECT * FROM cities WHERE {where}"
        rows = self.__get_all_from_db(query)
        return {row[0]: self.__formatted_city(row) for row in rows}

    def __get_region_by_filter(self, where: str) -> dict:
        query = f"SELECT * FROM regions WHERE {where}"
        rows = self.__get_all_from_db(query)
        return {row[0]: self.__formatted_region(row) for row in rows}

    def __get_user_by_filter(self, where: str) -> dict:
        query = f"SELECT * FROM users WHERE {where}"
        rows = self.__get_all_from_db(query)
        return {row[0]: self.__formatted_user(row) for row in rows}

    def __formatted_city(self, row):
        return {
            "id": row[0],
            "region_id": row[1],
            "city_name": row[2]
        }

    def __formatted_region(self, row):
        return {
            "id": row[0],
            "region_name": row[1]
        }

    def __formatted_user(self, row):
        return {
            "id": row[0],
            "second_name": row[1],
            "first_name": row[2],
            "patronymic": row[3],
            "region_id": row[4],
            "city_id": row[5],
            "phone": row[6],
            "email": row[7]
        }

    def __write_data_to_db(self, query, data) -> bool:
        connection = self.create_connection()
        try:
            with connection:
                connection.executemany(query, data)
        except sqlite3.IntegrityError as err:
            print('Возникла ошибка: ', err)
            return False
        else:
            print('Запись данных прошла успешно')
            return True


if __name__ == '__main__':
    db = Db('test.db')
    if not db.does_db_exist():
        db.create_db()

    pprint(db.get_region_by_name("Краснодарский край"))
    pprint(db.get_city_by_name("Кропоткин"))
