# return r.status_code
# print(extract(0))
# def transform(soup):  #// we check if the table works or section works STEP 1
#     divs = soup.find_all('div',class_='.property-inner')
#     return len(divs)
# c =extract(0)
# print(transform(c))
# def transform(soup):
#     divs = soup.find_all('div',class_='wp-block-title hidden-xs')
#     for item in divs:
#         title  = item.find('h3').text.strip()
#         price = item.find('span',class_= 'pull-sm-left').text
#         print(price)
#     return
#
# c = extract(0)


# import numpy as np
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv
from bs4 import BeautifulSoup
import requests
from csv import  writer
# #
# #
# print('Lekki')
#
for x in range(1,2):

    baseurl = f"https://www.property24.com.ng/3-bedroom-properties-for-sale-in-ikoyi-obalende-c1298?Page={x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser', )
    # print(soup)
    lists = soup.find_all("div", class_="propertyTileWrapper", limit=None)
    print(len(lists))

    for list in lists:
        title = list.find('div', class_="area left").text.strip()
        price = list.find('span', class_="price").text.strip().replace('₦ ','').replace(' ','')
        location = list.find('div', class_="left address").text.strip()
        try:
            bedrooms = list.find('span', class_="left").text
        except:
            bedrooms = 'N/A'

        description = list.find('div', class_="left description").text.strip().replace('\r', '').replace('...', '')

        info = [title, price, location, bedrooms]


        with open("Ikoyi24lllll.csv", "w", encoding='utf8', newline='') as f:
            thewriter = writer(f)
            header = ['title', 'price', 'location', 'bedrooms']
            thewriter.writerow(header)
            thewriter.writerow(info)






for x in range(0,10):

    baseurl = f"https://www.property24.com.ng/3-bedroom-properties-for-sale-in-lekki-c1316?Page={x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl )
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser', )
    # print(soup)
    lists = soup.find_all("div", class_="propertyTileWrapper", limit=None)
    print(len(lists))
    with open("lekki24lllll.csv", "w", encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header =   ['title','price','location','bedrooms']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('div', class_="area left").text.strip()
            price = list.find('span', class_="price").text.strip().replace('₦ ','').replace(' ','')
            location = list.find('div', class_="left address").text.strip()
            try:
                bedrooms = list.find('span', class_="left").text
            except:
                bedrooms = 'N/A'

            description = list.find('div', class_="left description").text.strip().replace('\r', '').replace('...', '')
            info = [title,price,location,bedrooms]
            thewriter.writerow(info)


import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import csv
from bs4 import BeautifulSoup
import requests
from csv import writer

#
#
print('Vi')

for x in range(0,2):

    baseurl = f"https://www.property24.com.ng/3-bedroom-properties-for-sale-in-victoria-island-s15807?Page={x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser', )
    # print(soup)
    lists = soup.find_all("div", class_="propertyTileWrapper", limit=None)
    print(len(lists))
    with open("Vi24lol.csv", "w", encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['title', 'price', 'location', 'bedrooms']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('div', class_="area left").text.strip()
            price = list.find('span', class_="price").text.strip().replace('₦ ', '').replace(' ', '')
            location = list.find('div', class_="left address").text.strip()
            try:
                bedrooms = list.find('span', class_="left").text
            except:
                bedrooms = 'N/A'

            description = list.find('div', class_="left description").text.strip().replace('\r', '').replace('...', '')
            info = [title, price, location, bedrooms]
            thewriter.writerow(info)
#
print('Ikeja')

for x in range(0,10):

    baseurl = f"https://www.property24.com.ng/3-bedroom-properties-for-sale-in-ikeja-c1305?Page={x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl , verify=False)
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    lists = soup.find_all("div", class_="propertyTileWrapper", limit=None)
    print(len(lists))
    with open("Ikeja24.csv", "w", encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header =   ['title','price','location','bedrooms']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('div', class_="area left").text.strip()
            price = list.find('span', class_="price").text.strip().replace('₦ ','').replace(' ','')
            location = list.find('div', class_="left address").text.strip()
            try:
                bedrooms = list.find('span', class_="left").text
            except:
                bedrooms = 'N/A'

            description = list.find('div', class_="left description").text.strip().replace('\r', '').replace('...', '')
            info = [title,price,location,bedrooms]
            thewriter.writerow(info)



# aaaaaaAAAAAAAAAAaaa

print('Ikeja')

for x in range(1,5):

    baseurl = f"https://https://www.property24.com.ng/3-bedroom-properties-for-sale-in-ikeja-c1305?Page={x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl , verify=False)
    # print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    lists = soup.find_all("div", class_="propertyTileWrapper", limit=None)
    print(len(lists))
    with open("Ikeja24.csv", "w", encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header =   ['title','price','location','bedrooms']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('div', class_="area left").text.strip()
            price = list.find('span', class_="price").text.strip().replace('₦ ','').replace(' ','')
            location = list.find('div', class_="left address").text.strip()
            try:
                bedrooms = list.find('span', class_="left").text
            except:
                bedrooms = 'N/A'

            description = list.find('div', class_="left description").text.strip().replace('\r', '').replace('...', '')
            info = [title,price,location,bedrooms]
            thewriter.writerow(info)





