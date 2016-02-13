# -*- coding: utf-8 -*-

## BeautifulSoup example code

__author__ = 'agun'
from bs4 import BeautifulSoup
import requests
import MySQLdb as mdb

def stripHtmlTags(htmlTxt):
    if htmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt, "html.parser").findAll(text=True))

con = mdb.connect('localhost', 'root', '', 'kisa')
with con:
    cur = con.cursor()
    cur.execute("SELECT url_id, url  FROM RssUrl")
    rows = cur.fetchall()
    for row in rows:
        r  = requests.get(row[1])
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        for item in soup.find_all('item'):
            title = str(item.title.string).replace("'","");
            title = str(item.title.string).replace("'","");
            description = str(item.description.string).replace("'","");
            description = str(item.description.string).replace("'","");
            print(title)
            print(stripHtmlTags(description))