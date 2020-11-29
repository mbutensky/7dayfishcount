import requests
from bs4 import BeautifulSoup

url = ('view-source:https://www.fpc.org/currentdaily/HistFishTwo_7day-ytd_Adults.htm')
page = requests.get(url).text
print(page)