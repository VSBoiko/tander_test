import pandas


class ExcelWorker:
    @staticmethod
    def get_rows(filename: str, sheet_name: str) -> list:
        rows = pandas.read_excel(filename, sheet_name=sheet_name)
        return rows.to_dict(orient="records")

    @staticmethod
    def create_user_xlsx(filename: str, sheet_name: str, columns: list, users: list):
        data = [[user.get(column) for column in columns] for user in users]
        return ExcelWorker.create_xlsx(
            filename=filename,
            sheet_name=sheet_name,
            columns=columns,
            data=data
        )

    @staticmethod
    def create_xlsx(filename: str, sheet_name: str,
                    columns: list, data: list):
        try:
            df = pandas.DataFrame(data, columns=columns)
            df.to_excel(filename, sheet_name=sheet_name)
        except Exception as err:
            # log
            return False
        else:
            return True
