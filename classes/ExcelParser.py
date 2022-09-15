import pandas


class ExcelParser:
    def __init__(self, filename: str):
        self.__filename = filename

    def get_filename(self) -> str:
        return self.__filename

    def get_rows(self, sheet_name: str) -> list:
        rows = pandas.read_excel(self.get_filename(), sheet_name=sheet_name)
        return rows.to_dict(orient="records")
