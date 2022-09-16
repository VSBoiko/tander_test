from classes.ExcelWorker import ExcelWorker
from classes.Db import Db
from classes.PdfWorker import PdfWorker


class App:
    @staticmethod
    def create_db(name: str, script: str):
        db = Db(name, script)
        if not db.does_db_exist():
            db.create_db()

        return db

    @staticmethod
    def add_users_from_excel(excel: str, sheet: str, db):
        new_users = ExcelWorker.get_rows(excel, sheet)
        for user in new_users:
            region = db.get_region_by_name(user["region_name"].strip()).pop()
            city = db.get_city_by_name(user["city_name"].strip()).pop()
            db.add_user(
                second_name=user["second_name"].strip(),
                first_name=user["first_name"].strip(),
                patronymic=user["patronymic"].strip(),
                region_id=int(region.get("id")),
                city_id=int(city.get("id")),
                phone=user["phone"].strip(),
                email=user["email"].strip()
            )

    @staticmethod
    def create_excel_with_users(db, excel: str, sheet: str):
        users = db.get_all_users()
        regions = db.get_all_regions()
        cities = db.get_all_cities()

        columns = [
            "second_name",
            "first_name",
            "patronymic",
            "region_name",
            "city_name",
            "phone",
            "email"
        ]
        for key, user in enumerate(users):
            region = list(filter(lambda x: x.get("id") == user.get("region_id"), regions)).pop()
            city = list(filter(lambda x: x.get("id") == user.get("city_id"), cities)).pop()
            users[key].update({
                "region_name": region.get("region_name"),
                "city_name": city.get("city_name"),
            })

        ExcelWorker.create_user_xlsx(excel, sheet, columns, users)

    @staticmethod
    def add_user_from_my_resume(db, pdf: str):
        text = PdfWorker.get_pdf_text(pdf)
        text_list = text.split("\n")
        name = text_list[0].split()
        phone = text_list[text_list.index("Номер телефона:")+1].strip()
        email = text_list[text_list.index("Электронная почта:")+1].strip()
        living_place = text_list[text_list.index("Город проживания:")+1].split(", ")
        city = db.get_city_by_name(living_place[0].strip())
        region = db.get_region_by_name(living_place[1].strip())
        me_user = {
            "second_name": name[0].strip(),
            "first_name": name[1].strip(),
            "patronymic": name[2].strip(),
            "region_id": region[0].get("id"),
            "city_id": city[0].get("id"),
            "phone": phone,
            "email": email
        }

        db.add_user(**me_user)
