from dataHandler.MysqlHandler import DataHandler
from dataHandler.DataCollector import DataCollector

import os
dbUser = os.environ["DB_USER"]
dbPw = os.environ["DB_PW"]

dataHandler = DataHandler("localhost", dbUser, dbPw, "kisa");

def rssFetch(url_id, rssData):
    linkData = dataHandler.getRssdataByLink(rssData["link"])
    if len(linkData) == 0 :
        dataHandler.insertRssData('',rssData["title"], rssData["link"], rssData["pubDate"], rssData["description"], url_id)


dataCollector = DataCollector();
urlList = dataHandler.getUrl();

for url in urlList:
    dataCollector.getRss(url[2], url[0], rssFetch)
