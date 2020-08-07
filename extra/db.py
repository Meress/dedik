#!/usr/bin/python 3.8.2
import psycopg2

con = psycopg2.connect(
    database="postgres_db",
    user="postgres_user",
    password="PasswordWithExtraSecurity",
    host="localhost",
    # port="5432:5432"
)
print("Database opened successfully")

cur = con.cursor()
# cur.execute('''CREATE TABLE Pandora
#      (ID INT PRIMARY KEY NOT NULL,
#      S_NAME TEXT NOT NULL,
#      P_NAME TEXT NOT NULL,
#      DATA_TIME timestamp);''')
#
# print("Table created successfully")
# con.commit()

# cur.execute("INSERT INTO Pandora (ID, S_NAME, P_NAME, DATA_TIME) VALUES (%s,%s,%s,%s)",
#             ("5", "SSS", "PPP", "05.05.2005 10:10"))
# con.commit()
cur.execute("SELECT ID, S_NAME, P_NAME from Pandora")
rows = cur.fetchall()
print(rows)

con.commit()
cur.close()
con.close()
