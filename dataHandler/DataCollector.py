__author__ = 'agun'

from bs4 import BeautifulSoup
import requests


def stripHtmlTags(htmlTxt):
    if htmlTxt is None:
        return None
    else:
        return ''.join(BeautifulSoup(htmlTxt, "html.parser").findAll(text=True))

class DataCollector(object):

    def getRss(self, url, url_id, fetchFun):
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        for item in soup.find_all('item'):
            title = str(item.title.string).replace("'","");
            description = str(item.description.string).replace("'","");

            rssData = {
                'title': title,
                'url_id': url_id,
                'link': str(item.link.string),
                'pubDate': str(item.pubdate.string),
                'description': description,
            }
            fetchFun(url_id, rssData)

