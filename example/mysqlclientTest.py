# -*- coding: utf-8 -*-
## mysql client example code

__author__ = 'agun'
import MySQLdb as mdb
con = mdb.connect('localhost', 'root', '', 'kisa')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM RssData")
    rows = cur.fetchall()

    for row in rows:
        print(row)