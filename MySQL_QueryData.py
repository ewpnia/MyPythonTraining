# -*- coding: utf-8 -*-
import datetime
import mysql.connector

config = {
    "user": "root",
    "password": "123456",
    "host": "127.0.0.1",
    "database": "ForPython",
    "raise_on_warnings": True,
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
# query = ("SELECT ID, Name, Color from Fruits"
#          "WHERE SellsTime BETWEEN %s AND %s")
# SellsTime_start = datetime.date(2013,1,1)
# SellsTime_end = datetime.date(2013,12,31)
# cursor.execute(query, (SellsTime_start, SellsTime_end))

query = ("SELECT ID, Name, Color from Fruits")
cursor.execute(query)

for (ID, Name, Color) in cursor:
    # print("{}, {} was sold on {:%d %b %b}".format(
    #     ID, Name, Color))
    print "%d, %s, %s" % (ID, Name, Color)

cursor.close()
cnx.close()