#!/usr/bin/python 3.8.2
import sys
import psycopg2
from flask import Flask
from flask import request

con = psycopg2.connect(
    database="postgres_db",
    user="postgres_user",
    password="PasswordWithExtraSecurity",
    host="postgres",
    port="5432:5432"
)
print("Database opened successfully")

# cur = con.cursor()
# cur.execute('''CREATE TABLE Pandora2
#      (ID SERIAL,
#      S_NAME TEXT NOT NULL,
#      P_NAME TEXT NOT NULL);''')
#
# print("Table created successfully")
# con.commit()


a = []
app = Flask(__name__)


@app.route("/post", methods=['POST'])
def post():
    if request.method == 'POST':
        a = []
        d = []
        f = str(request.form)
        k = 0
        for i in f:
            if i == ';':
                k += 1
        if k >= 2:
            f = str(request.form).split(';')
            f = f[1]
            a.append(f)

            ############################
            d = a[0].split('::')
            y = open("kodes.csv", "r")
            c = y.read().splitlines()

            for i in c:
                v = i.split(';')
                if v[0] == d[0]:
                    d[0] = v[1]
                    # print(v[0], file=sys.stderr)
                    # print(d[0], file=sys.stderr)
                    # print(v[1], file=sys.stderr)
            z = open("stores.txt", "r")
            m = z.read().splitlines()

            for i in m:
                w = i.split(';')
                if w[0] == d[1]:
                    d[1] = w[1]
                    # print(w[0], file=sys.stderr)
                    # print(d[1], file=sys.stderr)
                    # print(w[1], file=sys.stderr)
            cur = con.cursor()
            # cur.execute('''CREATE TABLE Pandora2
            #      (ID SERIAL,
            #      S_NAME TEXT NOT NULL,
            #      P_NAME TEXT NOT NULL);''')
            #
            # print("Table created successfully")
            # con.commit()

            cur.execute("INSERT INTO Pandora2 (S_NAME, P_NAME) VALUES (%s,%s)",
                        (d[1], d[0]))

            cur.execute("SELECT ID, S_NAME, P_NAME from Pandora2")
            rows = cur.fetchall()
            print(rows, file=sys.stderr)

            con.commit()
            cur.close()
            ##################################
            return str(a)
        else:
            return str(a)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)

# d = []
# f = open("log.csv", "r+")
# s = f.read().splitlines()
# d = a.split('::')
# for item in s:
#     a = item.split(';')
#     if len(a) >= 4 and a[2] == " SIMCOM_MODULE":
#         del a[1]
#         del a[1]
#         x = a[1].split('=')
#         a[1] = x[1]
#         b = x[1].split('/')
#         a[1:2] = b
#         d.append(a[0:3])
#
# y = open("kodes.csv", "r")
# c = y.read().splitlines()
#
# for item in d:
#     for i in c:
#         v = i.split(';')
#         p = item[0]
#         if len(p) > 0 and v[0] == p:
#             item[2] = v[1]
#
# z = open("stores.txt", "r")
# m = z.read().splitlines()
#
# for item in d:
#     for i in m:
#         w = i.split(';')
#         p = item[1]
#         if len(p) > 0 and w[0] == p:
#             # print(item[1])
#             # print(w[1])
#             item[1] = w[1]

# print(d)
# print(len(d))
# f.close()

# cur = con.cursor()
# cur.execute('''CREATE TABLE Pandora6
#      (ID SERIAL,
#      S_NAME TEXT NOT NULL,
#      P_NAME TEXT NOT NULL);''')
#
# print("Table created successfully")
# con.commit()
#
# # k = 1
# j = 0
# for i in d:
#     a = d[j]
#     cur.execute("INSERT INTO Pandora6 (S_NAME, P_NAME) VALUES (%s,%s,%s)",
#                 (a[1], a[0]))
#     # k = k + 1
#     j = j + 1
# cur.execute("SELECT ID, S_NAME, P_NAME, from Pandora6")
# rows = cur.fetchall()
# print(rows)
#
# con.commit()
# cur.close()
con.close()
