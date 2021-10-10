
from abc import abstractproperty
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv
from bs4 import BeautifulSoup as bs
import requests

URL = "https://www.property24.com.ng/3-bedroom-properties-for-sale-in-ikoyi-obalende-c1298?Page="

# for page in range(1,20):
#     print(page)

page = 1
req = requests.get(URL + str(page))
soup = bs(req.text, "html.parser")
# print(soup)
# Container = soup.find("div", class_="propertyTileWrapper", limit=None)
container = soup.find("div", attrs={'class', "propertyTileWrapper"})
apts = container.find_all("div", class_="propertyTileWrapper", limit=None)
# print(container)
for apt in apts:
    links = apt.find('div', class_="area left")
    title = ""
    try:
        links[8].text
    except:
        pass
    print ('title: %s' % (title))