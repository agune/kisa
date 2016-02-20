# -*- coding: utf-8 -*-
## mysql database bandle function
__author__ = 'agun'
import MySQLdb as mdb

class DataHandler(object):
    conn = None

    def __init__(self, host, user, pw, dbname):
        self.conn = mdb.connect(host, user, pw, dbname)


    def getUrl(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM RssUrl")
            rows = cur.fetchall()
            return rows

    def getRssdata(self, is_token):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM RssData WHERE is_token = %s", (is_token))
            rows = cur.fetchall()
            return rows

    def getRssText(self, is_token):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM RssText WHERE is_token = %s", (is_token))
            rows = cur.fetchall()
            return rows

    def insertRssData(self, author, title, link, pubDate, content, url_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO RssData (author, title, link, pubDate, content, url_id)VALUES(%s, %s, %s, %s, %s, %s)", (author, title, link, pubDate, content, url_id))

            return cur.lastrowid

    def insertRssText(self, rssId, content):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO RssText (rss_id, content)VALUES(%s, %s)", (rssId, content))



