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

d = []
f = open("log.csv", "r+")
s = f.read().splitlines()
for item in s:
    a = item.split(';')
    if len(a) >= 4 and a[2] == " SIMCOM_MODULE":
        del a[1]
        del a[1]
        x = a[1].split('=')
        a[1] = x[1]
        b = x[1].split('/')
        a[1:2] = b
        d.append(a[0:3])

y = open("kodes.csv", "r")
c = y.read().splitlines()

for item in d:
    for i in c:
        v = i.split(';')
        p = item[2]
        if len(p) > 0 and v[0] == p:
            item[2] = v[1]

z = open("stores.txt", "r")
m = z.read().splitlines()

for item in d:
    for i in m:
        w = i.split(';')
        p = item[1]
        if len(p) > 0 and w[0] == p:
            # print(item[1])
            # print(w[1])
            item[1] = w[1]

print(d)
print(len(d))
f.close()

cur = con.cursor()
# cur.execute('''CREATE TABLE Pandora4
#      (ID SERIAL,
#      S_NAME TEXT NOT NULL,
#      P_NAME TEXT NOT NULL,
#      DATA_TIME TEXT NOT NULL);''')
#
# print("Table created successfully")
# con.commit()

# k = 1
j = 0
for i in d:
    a = d[j]
    cur.execute("INSERT INTO Pandora4 (S_NAME, P_NAME, DATA_TIME) VALUES (%s,%s,%s)",
                (a[1], a[2], a[0]))
    # k = k + 1
    j = j + 1
cur.execute("SELECT ID, S_NAME, P_NAME, DATA_TIME from Pandora4")
rows = cur.fetchall()
print(rows)

con.commit()
cur.close()
con.close()
