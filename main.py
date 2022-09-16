from classes.App import App


if __name__ == '__main__':
    db = App.create_db("test.db", "script_create.sql")
    App.add_users_from_excel("new_users.xlsx", "Sheet1", db)
    App.create_excel_with_users(db, "db_users.xlsx", "Sheet255")
    App.add_user_from_my_resume(db, "resume.pdf")
