CREATE TABLE IF NOT EXISTS regions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  region_name TEXT
);

CREATE TABLE IF NOT EXISTS cities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  region_id INTEGER,
  city_name TEXT,
  FOREIGN KEY (region_id)  REFERENCES regions (id)
);

CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  second_name TEXT,
  first_name TEXT,
  patronymic TEXT,
  region_id INTEGER,
  city_id INTEGER,
  phone TEXT,
  email TEXT,
  FOREIGN KEY (region_id)  REFERENCES regions (id),
  FOREIGN KEY (city_id)  REFERENCES cities (id)
);

INSERT INTO regions (region_name) VALUES('Краснодарский край');
INSERT INTO regions (region_name) VALUES('Ростовская область');
INSERT INTO regions (region_name) VALUES('Ставропольский край');

INSERT INTO cities (region_id, city_name) VALUES(1, 'Краснодар');
INSERT INTO cities (region_id, city_name) VALUES(1, 'Кропоткин');
INSERT INTO cities (region_id, city_name) VALUES(1, 'Славянск');
INSERT INTO cities (region_id, city_name) VALUES(2, 'Ростов');
INSERT INTO cities (region_id, city_name) VALUES(2, 'Шахты');
INSERT INTO cities (region_id, city_name) VALUES(2, 'Батайск');
INSERT INTO cities (region_id, city_name) VALUES(3, 'Ставрополь');
INSERT INTO cities (region_id, city_name) VALUES(3, 'Пятигорск');
INSERT INTO cities (region_id, city_name) VALUES(3, 'Кисловодск');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Родионов', 'Денис', 'Донатович', 1, 1, '+7(495)802-90-55', 'pittokigoufi-7787@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Новиков', 'Никифор', 'Созонович', 1, 1, '+7(495)182-96-33', 'braufiwoireusseu-3458@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Колобов', 'Петр', 'Мэлсович', 1, 1, '+7(495)151-32-89', 'veifrazoixouhei-6963@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)

VALUES ('Ершов', 'Овидий', 'Иринеевич', 1, 2, '+7(495)039-72-25', 'veiniddottize-3601@yopmail.com');
Insert INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Юдин', 'Мирон', 'Константинович', 1, 2, '+7(495)381-43-67', 'truppuvaubaufra-2592@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Кононов', 'Гаянэ', 'Тимофеевич', 1, 2, '+7(495)505-23-84', 'vobrobreubrauho-2270@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Исаев', 'Василий', 'Вячеславович', 1, 3, '+7(495)469-75-87', 'joifrusehocrou-2240@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Ермаков', 'Модест', 'Викторович', 1, 3, '+7(495)263-59-97', 'hemullofeuco-5759@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Молчанов', 'Лаврентий', 'Евсеевич', 1, 3, '+7(495)786-15-46', 'lugrofreyegru-2019@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Мясников', 'Кондратий', 'Михаилович', 2, 4, '+7(495)094-16-36', 'trittelleissaufe-4014@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Новиков', 'Эрнест', 'Миронович', 2, 4, '+7(495)447-46-28', 'cruttemmoillirou-8182@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Новиков', 'Корнелий', 'Проклович', 2, 4, '+7(495)006-03-16', 'braufrugoufoilla-8168@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Симонов', 'Дмитрий', 'Валентинович', 2, 5, '+7(495)572-95-44', 'vifilegrehei-2152@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Жданов', 'Ян', 'Лукьянович', 2, 5, '+7(495)209-66-16', 'tannofreitracu-2799@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Соловьёв', 'Герман', 'Демьянович', 2, 5, '+7(495)428-99-15', 'breujauromoiffu-2852@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Фомин', 'Прохор', 'Улебович', 2, 6, '+7(495)766-30-25', 'grubricragraya-2695@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Носов', 'Лев', 'Станиславович', 2, 6, '+7(495)431-13-72', 'tofrikoupeuppe-4314@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Лукин', 'Мечислав', 'Всеволодович', 2, 6, '+7(495)404-54-62', 'gitriciheso-4458@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Ситников', 'Дмитрий', 'Дамирович', 3, 7, '+7(495)467-04-48', 'mufrauproinnutti-1032@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Беляков', 'Митрофан', 'Артёмович', 3, 7, '+7(495)289-43-38', 'nuneppogecru-7264@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Никифоров', 'Корней', 'Германнович', 3, 7, '+7(495)715-31-19', 'petobroquaque-8626@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Калашников', 'Федор', 'Эдуардович', 3, 8, '+7(495)650-03-31', 'sessawagozei-8169@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Лукин', 'Назарий', 'Степанович', 3, 8, '+7(495)098-53-70', 'jouzemedummi-8267@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Сафонов', 'Юлиан', 'Богданович', 3, 8, '+7(495)591-92-99', 'gazaprippefrei-6123@yopmail.com');

INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Комаров', 'Самуил', 'Глебович', 3, 9, '+7(495)054-26-31', 'quazoiwefraproi-5629@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Дементьев', 'Авраам', 'Михаилович', 3, 9, '+7(495)923-36-51', 'jayulebulli-3379@yopmail.com');
INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email)
VALUES ('Тимофеев', 'Фрол', 'Борисович', 3, 9, '+7(495)402-88-24', 'yoxoisoteiyau-3061@yopmail.com');
