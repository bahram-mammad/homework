# import psycopg2

# conn = psycopg2.connect("dbname=clinique user=postgres host=localhost password=123456")
# cur = conn.cursor()

# query = """
# CREATE TABLE department (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50) NOT NULL UNIQUE
# );
# CREATE TABLE doctor (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     department_id INT NOT NULL,
#     CONSTRAINT fk_department
#         FOREIGN KEY(department_id)
#             REFERENCES department(id)
#             ON DELETE CASCADE
# );
# CREATE TABLE shedule (
#     id SERIAL PRIMARY KEY,
#     start_time TIME,
#     end_time TIME,
#     doctor_id INT NOT NULL UNIQUE,
#     CONSTRAIT fk_doctor
#         FOREIGN KEY(doctor_id)
#             REFERENCES doctor(id)
#             ON DELETE CASCADE
# );
# CREATE TABLE category (
#     id SERIAL PRIMARY KEY,
#     content TEXT NOT NULL
# );
# CREATE TABLE article (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50) NOT NULL,
#     content VARCHAR(50) NOT NULL,
#     doctor_id INT NOT NULL,
#     category_id INT NOT NULL,
#     CONSTRAINT fk_doctor
#         FOREIGN KEY(doctor_id)
#             REFERENCES doctor(id)
#             ON DELETE CASCADE,
#     CONSTRAINT fk_category
#         FOREIGN KEY(category_id)
#             REFERENCES category(id)
#             ON DELETE CASCADE 
# );
# CREATE TABLE doctor_article (
#     id PRIMARY KEY SERIAL,
#     article_id INT NOT NULL, 
#     doctor_id INT NOT NULL,
#     CONSTRAINT fk_article
#         FOREIGN KEY(article_id)
#             REFERENCES article(id)
#             ON DELETE CASCADE, 
#     CONSTRAINT fk_doctor
#         FOREIGN KEY(doctor_id)
#             REFERENCES doctor(id)
#             ON DELETE CASCADE 
# );
# """

# cur.execute(query)
# conn.commit()


# -----------------------------------------------------------

# import psycopg2
# import datetime

# date = datetime.date(2022, 7, 10)
# conn = psycopg2.connect("dbname=information user=postgres host=localhost password=123456")
# cur = conn.cursor()


# def show(cursor):
#     length = 17    
#     print(*[desc[0].ljust(length) for desc in cursor.description], sep= '')
#     print('-'*150)
#     result = cursor.fetchall()
#     for row in result:
#         for col in row:
#           print(str(col).ljust(length)[:17], end = '')
#         print()   


# # Qeyd bu gunun tarixini 2022-07-10 olaraq nəzərə alın:
# #1) ABB ASC şirkətinə aid elanları göstərin
# #2) ABB ASC şirkətinə aid 2000-dən az maşa sahib elanları göstərin
# #3) Kontakt Home şirkətinə aid vaxtı keçmiş elanları göstərin
# #4) Xarici dil tələb etməyən 2500+ maaşlı iş elanlarını göstərin
# #5) Sonu proqramçı ilə bitən iş elanlarını göstərin
# #6) Adında “end” keçməyən iş elanlarını göstərin
# #7) İT və ya IT ilə başlayan iş elanlarını göstərin
# #8) Xarici dil tələb edən iş elanlarını maaşı çoxdan aza olmaq üzrə sıralayın
# #9) Ən çox maaş verən ilk elanı göstərin
# #10) Tarixi keçməmiş iş elanlarını bitmə tarixinə görə tezdən gecə sıralayıb, 2-ci və 5-ci sıra arasında olanları göstərin
# #11)Daxilində developer və ya proqramçı keçib, xarici dil tələb etməyən elanları göstərin
# #12) Kontakt Home, AzəriMed QSC, A2Z Technologies şirkətlərindən birinə aid olub maaşı 2500 ilə 3000 arasında olan elanları göstərin
# #13) ABB ASC şirkətinin tarixi keçmiş elanlarının sayını göstərin
# #14) Xarici dil tələb etməyən elanlar arasında ən yüksək maaşı tapın
# #15) Xarici dil tələb edən elanlar arasında ən kiçik maaşı tapın
# #16) İçində developer və ya proqramçı keçən işlərin ortalama maaşını tapın
# #17) Kontakt Home, AzəriMed QSC, A2Z Technologies şirkətlərinin qeyd etdikləri maaşların cəmini tapın


# info_list = [
#     # basliq, sirket, maas, bitme tarixi, xarici dil telebi
#     ('iOS developer', 'A2Z Technologies', 3500, '2022-07-18', True),
#     ('Tender üzrə mütəxəssis', 'A2Z Technologies', 1500, '2022-06-11', False),
#     ('Məlumat bazası üzrə inzibatçı', 'ABB ASC', 1500, '2022-07-12', True),
#     ('Database Administrator', 'A2Z Technologies', 2500, '2022-07-14', True),
#     ('Front-End Developer', 'AzəriMed QSC', 1500, '2022-07-23', False),
#     ('Proqram təminatının testləşdirilməsi üzrə mühəndis','ABB ASC', 1500, '2022-08-10', False),
#     ('Back-end üzrə proqramçı', 'ABB ASC', 4100, '2022-07-11', True),
#     ('Biznes analitika üzrə Baş mütəxəssis ', 'ABB ASC', 2200, '2022-07-03', True),
#     ('Android proqramçı', 'ABB ASC', 1300, '2022-07-22', True),
#     ('Front-end üzrə proqramçı', 'ABB ASC', 3200, '2022-07-06', True),
#     ('Full stack PHP proqramçı', 'AzəriMed QSC', 2400, '2022-07-17', False),
#     ('Avtomatlaşdırılmış əməliyyat sistemi üzrə proqramçı','ABB ASC', 2700, '2022-07-15', True),
#     ('Proqram təminatı üzrə mühəndis', 'Kontakt Home', 2700, '2022-07-13', False),
#     ('Hüquqşünas', 'Kontakt Home', 1500, '2022-07-03', False),
#     ('Çatdırılma xidmətləri üzrə fəhlə', 'Kontakt Home', 500, '2022-07-15', True),
#     ('PHP developer', 'ARIS', 1500, '2022-07-11', True),
#     ('Məhsul üzrə menecer', 'Kontakt Home', 2800, '2022-07-05', True),
#     ('Proqram təminatı üzrə aparıcı mühəndis','Kontakt Home', 2500, '2022-07-02', False),
#     ('İT sənədləşməsi üzrə mütəxəssis', 'Azericard', 1500, '2022-07-25', True),
#     ('Information Security Specialist', 'DEFSCOPE LLC', 2500, '2022-07-03', False),
#     ('IT Helpdesk', 'Azericard', 1500, '2022-07-30', True),
#     ('Cybersecurity Business Development Internship','DEFSCOPE LLC', 2900, '2022-07-19', False),
#     ('Vue.js developer', 'ARIS', 1500, '2022-07-29', True),
# ]


# query = """
# CREATE TABLE inform (
#     title VARCHAR(200) NOT NULL,
#     company VARCHAR(50) NOT NULL,
#     salary NUMERIC,
#     expire_date DATE,
#     foreign_lang BOOLEAN
# );
# """
 
# query = """INSERT INTO inform (title, company, salary, expire_date, foreign_lang) VALUES (%s, %s, %s, %s, %s)"""  
# for inform in info_list :   
#     cur.execute(query,inform)

# conn.commit()



# 1) 
# query = "SELECT * FROM inform WHERE company='ABB ASC';"
# 2)
# query = "SELECT * FROM inform WHERE company = 'ABB ASC' AND salary<2000;"
# 3)
# query = "SELECT * FROM inform WHERE company = 'Kontakt Home' AND expire_date>'2022-07-10';"
# 4)
# query = "SELECT * FROM inform WHERE foreign_lang = 'False' AND salary>2500;"
# 5)
# query = "SELECT * FROM inform WHERE title LIKE '%proqramçı';"
# 6)
# query = "SELECT * FROM inform WHERE title NOT LIKE '%end';"
# 7)
# query = "SELECT * FROM inform WHERE title LIKE 'İT%' OR title LIKE 'IT%';"
# 8)
# query = "SELECT * FROM inform WHERE foreign_lang = 'True' ORDER BY salary DESC;"
# 9)
# query = "SELECT * FROM inform ORDER BY salary DESC LIMIT 1;"
# 10)
# query = "SELECT * FROM inform WHERE expire_date>'2022-07-10' ORDER BY expire_date OFFSET 5-3 LIMIT 2;"
# 11)
# query = "SELECT * FROM inform WHERE title  LIKE '%developer%' OR title LIKE '%proqramçı%' AND foreign_lang='False';" ?
# 12)
# query = "SELECT * FROM inform WHERE company ~ '^[AK][%oz2%][%nə%Z].+$' AND salary BETWEEN 2500 AND 3000;"
# 13)
# query = "SELECT * FROM inform WHERE company = 'ABB ASC' AND expire_date>'2022-07-10';"
# 14)
# query = "SELECT * FROM inform WHERE foreign_lang = 'False' ORDER BY salary DESC LIMIT 1;"
# 15)
# query = "SELECT * FROM inform WHERE foreign_lang = 'True' ORDER BY salary LIMIT 1;"
# 16)
# query = "SELECT ROUND(AVG(salary), 2) FROM inform WHERE title  LIKE '%developer%' OR title LIKE '%proqramçı%'"
# 17)
# query = "SELECT SUM(salary) FROM inform WHERE company ~ '^[AK][%oz2%][%nə%Z].+$';"

# cur.execute(query)
# show(cur)
