from classes.Db import Db


if __name__ == '__main__':
    db = Db("test.db", "script_create.sql")
    if not db.does_db_exist():
        db.create_db()
