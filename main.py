from pprint import pprint

from classes.Db import Db
from classes.ExcelWorker import ExcelWorker


if __name__ == '__main__':
    db = Db("test.db", "script_create.sql")
    if not db.does_db_exist():
        db.create_db()

    # new_users = ExcelParser.get_rows("new_users.xlsx", "Sheet1")
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

    # users = db.get_all_users()
    # regions = db.get_all_regions()
    # cities = db.get_all_cities()
    #
    # columns = [
    #     "second_name",
    #     "first_name",
    #     "patronymic",
    #     "region_name",
    #     "city_name",
    #     "phone",
    #     "email"
    # ]
    # for key, user in enumerate(users):
    #     region = list(filter(lambda x: x.get("id") == user.get("region_id"), regions)).pop()
    #     city = list(filter(lambda x: x.get("id") == user.get("city_id"), cities)).pop()
    #     users[key].update({
    #         "region_name": region.get("region_name"),
    #         "city_name": city.get("city_name"),
    #     })
    #
    # ExcelWorker.create_user_xlsx("test.xlsx", "Sheet255", columns, users)
