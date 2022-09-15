from pprint import pprint

from classes.Db import Db
from classes.ExcelParser import ExcelParser


if __name__ == '__main__':
    db = Db("test.db", "script_create.sql")
    if not db.does_db_exist():
        db.create_db()

    # parser = ExcelParser("new_users.xlsx")
    # new_users = parser.get_rows("Sheet1")
    # for user in new_users:
    #     region = db.get_region_by_name(user["region_name"].strip()).pop()
    #     city = db.get_city_by_name(user["city_name"].strip()).pop()
    #     db.add_user(
    #         second_name=user["second_name"].strip(),
    #         first_name=user["first_name"].strip(),
    #         patronymic=user["patronymic"].strip(),
    #         region_id=int(region.get("id")),
    #         city_id=int(city.get("id")),
    #         phone=user["phone"].strip(),
    #         email=user["email"].strip()
    #     )

