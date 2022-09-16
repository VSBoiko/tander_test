from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import DecodedStreamObject, EncodedStreamObject

from pprint import pprint

from classes.Db import Db
from classes.ExcelWorker import ExcelWorker


class PdfWorker:
    @staticmethod
    def get_pdf_text(filename: str):
        pdf = PdfFileReader(filename)
        pdf_text = ""
        for page in pdf.pages:
            print(page.get_contents())
            pdf_text += page.extractText()
        return pdf_text

    @staticmethod
    def replace_text_in_pdf(content, replacements=dict()):
        lines = content.splitlines()

        result = ""
        in_text = False

        for line in lines:
            print(line)
            if line == "BT":
                in_text = True

            elif line == "ET":
                in_text = False

            elif in_text:
                cmd = line[-2:]
                if cmd.lower() == 'tj':
                    replaced_line = line
                    for k, v in replacements.items():
                        replaced_line = replaced_line.replace(k, v)
                    result += replaced_line + "\n"
                else:
                    result += line + "\n"
                continue

            result += line + "\n"
        return result

    @staticmethod
    def process_data(object, replacements):
        data = object.getData()
        decoded_data = data.decode('utf-8')

        replaced_data = PdfWorker.replace_text_in_pdf(decoded_data, replacements)

        encoded_data = replaced_data.encode('utf-8')
        if object.decodedSelf is not None:
            object.decodedSelf.setData(encoded_data)
        else:
            object.setData(encoded_data)


if __name__ == '__main__':
    db = Db("test.db", "script_create.sql")
    if not db.does_db_exist():
        db.create_db()

    # new_users = ExcelWorker.get_rows("new_users.xlsx", "Sheet1")
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
    # ExcelWorker.create_user_xlsx("db_users.xlsx", "Sheet255", columns, users)

    # text = PdfWorker.get_pdf_text("resume.pdf")
    # text_list = text.split("\n")
    # name = text_list[0].split()
    # phone = text_list[text_list.index("Номер телефона:")+1].strip()
    # email = text_list[text_list.index("Электронная почта:")+1].strip()
    # living_place = text_list[text_list.index("Город проживания:")+1].split(", ")
    # city = db.get_city_by_name(living_place[0].strip())
    # region = db.get_region_by_name(living_place[1].strip())
    # me_user = {
    #     "second_name": name[0].strip(),
    #     "first_name": name[1].strip(),
    #     "patronymic": name[2].strip(),
    #     "region_id": region[0].get("id"),
    #     "city_id": city[0].get("id"),
    #     "phone": phone,
    #     "email": email
    # }
    #
    # db.add_user(**me_user)

    # PdfWorker.get_pdf_text("resume_template.pdf")
    users = db.get_all_users()
    regions = db.get_all_regions()
    cities = db.get_all_cities()
    pdf = PdfFileReader("resume_template.pdf")
    for user in users[0:1]:
        region_id = user.get("region_id")
        city_id = user.get("city_id")
        replacements = {
            "{second_name}": user.get("second_name"),
            "{first_name}": user.get("first_name"),
            "{patronymic}": user.get("patronymic"),
            "{region_name}": regions[region_id].get("region_name"),
            "{city_name}": cities[city_id].get("city_name"),
            "{phone}": user.get("phone"),
            "{email}": user.get("email")
        }
        writer = PdfFileWriter()
        for page_number in range(0, pdf.getNumPages()):

            page = pdf.getPage(page_number)
            contents = page.getContents()
            pprint(page)
            if isinstance(contents, DecodedStreamObject) or isinstance(contents, EncodedStreamObject):
                PdfWorker.process_data(contents, replacements)
            elif len(contents) > 0:
                for obj in contents:
                    if isinstance(obj, DecodedStreamObject) or isinstance(obj, EncodedStreamObject):
                        streamObj = obj.getObject()
                        PdfWorker.process_data(streamObj, replacements)

            writer.addPage(page)

        with open(f"{user.get('second_name')}_{user.get('first_name')}_"
                  f"{user.get('patronymic')}_resume.pdf", 'wb') as out_file:
            writer.write(out_file)
