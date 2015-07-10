# -*- coding: utf-8 -*-

# 基本连接
# import mysql.connector
# cnx = mysql.connector.connect(user = "root", password = "523164", 
#                                 host = "127.0.0.1", database = "ForPython")

# cnx.close()


# 提交连接错误
# import mysql.connector
# from mysql.connector import errorcode

# try:
#     cnx = mysql.connector.connect(user = "root", database = "ForPython")
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exists")
#     else:
#         print(err)
# else:
#     cnx.close()


# 连接参数较多时使用字典，注意**
import mysql.connector

config = {
    "user": "root",
    "password": "523164",
    "host": "127.0.0.1",
    "database": "ForPython",
    "raise_on_warnings": True,
}

cnx = mysql.connector.connect(**config)
cnx.close()