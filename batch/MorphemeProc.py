from analysis.Morpheme import Morpheme
from dataHandler.MysqlHandler import DataHandler


import os
dbUser = os.environ["DB_USER"]
dbPw = os.environ["DB_PW"]

dataHandler = DataHandler("localhost", dbUser, dbPw, "kisa");


morpheme = Morpheme()

rssDataList = dataHandler.getRssdata("0")


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def filterToken(var):
    if len(var) > 2 and isNumber(var) == False :
        return True
    return False


for rssData in rssDataList :

    if(rssData[1] != None and rssData[1] != "" and len(rssData[1]) > 2) :
        nouns = morpheme.nouns(rssData[1])
        tokenTitle = list(filter(filterToken, nouns))
        for(item) in tokenTitle:
            dataHandler.insertTitleToken(rssData[0], item)


    if(rssData[4] != None and rssData[4] != "" and len(rssData[4]) > 2) :
        nouns = morpheme.nouns(rssData[4])
        tokenContent = list(filter(filterToken, nouns))
        for(item) in tokenContent:
            dataHandler.insertContentToken(rssData[0], item)

    dataHandler.updateRssToken(rssData[0], "1")