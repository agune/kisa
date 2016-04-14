# -*- coding: utf-8 -*-
## mysql database bandle function
__author__ = 'agun'
import pymysql as mdb

class DataHandler(object):
    conn = None

    def __init__(self, host, user, pw, dbname):
        self.conn = mdb.connect(host=host, user=user, password=pw, db=dbname, charset='utf8mb4')


    def getUrl(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT url_id, vander, url  FROM RssUrl")
            rows = cur.fetchall()
            return rows

    def getRssdata(self, is_token):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, title, link, pubDate, content, url_id FROM RssData WHERE is_token = %s", (is_token))
            rows = cur.fetchall()
            return rows

    def getRssdataByLink(self, link):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, title, link, pubDate, content, url_id FROM RssData WHERE link = %s", (link))
            rows = cur.fetchall()
            return rows

    def getRssText(self, is_token):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM RssText WHERE is_token = %s", (is_token))
            rows = cur.fetchall()
            return rows


    def getTokenTitle(self, limit):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, rss_id, term  FROM tokenTitle order by id desc limit %s", (limit))
            rows = cur.fetchall()
            return rows

    def getKeywordIndex(self, term):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id FROM keyword_index WHERE term = %s", (term))
            rows = cur.fetchall()
            return rows

    def insertKeywordIndex(self, term):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO keyword_index (term)VALUES(%s)", (term))

            return cur.lastrowid

    def insertRelatedDoc(self, rss_id, doc_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT IGNORE INTO ralated_doc (rss_id, doc_id)VALUES(%s, %s)", (rss_id, doc_id))

    def insertRelatedTopic(self, rss_id, topic_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT IGNORE INTO related_topic (rss_id, topic)VALUES(%s, %s)", (rss_id, topic_id))


    def insertRssData(self, author, title, link, pubDate, content, url_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO RssData (author, title, link, pubDate, content, url_id)VALUES(%s, %s, %s, %s, %s, %s)", (author, title, link, pubDate, content, url_id))

            return cur.lastrowid

    def insertRssText(self, rssId, content):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO RssText (rss_id, content)VALUES(%s, %s)", (rssId, content))

    def insertTitleToken(self, rssId, term):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO tokenTitle (rss_id, term)VALUES(%s, %s)", (rssId, term))


    def insertContentToken(self, rssId, term):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("INSERT INTO tokenContent (rss_id, term)VALUES(%s, %s)", (rssId, term))


    def updateRssToken(self, rssId, isToken):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("UPDATE RssData set is_token = %s WHERE id = %s", (isToken, rssId))



