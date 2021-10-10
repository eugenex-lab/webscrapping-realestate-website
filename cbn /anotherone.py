import smtplib
from email.message import EmailMessage

import urllib3

from bs4 import BeautifulSoup
import requests
from csv import  writer

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#------------------------------------------------------------------------------------------------------------------------------------
print('Lekki 3 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/lekki?bedrooms=3&added=7&q=for-sale+flats-apartments+lagos+lekki+3+bedrooms+added+last+7+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("lek3.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



# msg = EmailMessage()
# msg['Subject'] = 'This is my first Python email'
# msg['From'] = 'kolapo.eugene@gmail.com'
# msg['To'] = 'eugene@sankore.com'
# msg.set_content('livid.csv')
#
#
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login('kolapo.eugene@gmail.com', '007Tomking')
#     smtp.send_message(msg)
#------------------------------------------------------------------------------------------------------------------------------------
print('Lekki 4 bedroom')
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/lekki?bedrooms=4&added=14&q=for-sale+flats-apartments+lagos+lekki+4+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("lekki4.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------
print('Lekki 5 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/lekki?bedrooms=5&added=30&q=for-sale+flats-apartments+lagos+lekki+5+bedrooms+added+last+30+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)



    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("lekki5.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------
print('VI 3 bedroom')
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/victoria-island?bedrooms=3&added=14&q=for-sale+flats-apartments+lagos+victoria-island+3+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)



    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("Vi3.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)

print('Above VI 4  bedroom')
#------------------------------------------------------------------------------------------------------------------------------------
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/victoria-island?bedrooms=4&added=14&q=for-sale+flats-apartments+lagos+victoria-island+4+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)



    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("Vi4.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)


#------------------------------------------------------------------------------------------------------------------------------------
print('Above VI 5  bedroom')
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/victoria-island?bedrooms=5&added=14&q=for-sale+flats-apartments+lagos+victoria-island+5+bedrooms+added+last+30+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)

    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("Vi5.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------
print('Above IKoyi 3  bedroom')
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/ikoyi?bedrooms=3&added=14&q=for-sale+flats-apartments+lagos+ikoyi+3+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("ikoyi3.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------

print('Above IKoyi 4  bedroom')
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/ikoyi?bedrooms=4&added=14&q=for-sale+flats-apartments+lagos+ikoyi+4+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("ikoyi4.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)


#------------------------------------------------------------------------------------------------------------------------------------

print('Above IKoyi 5  bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/lagos/ikoyi?bedrooms=5&added=30&q=for-sale+lagos+ikoyi+5+bedrooms+added+last+30+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("ikoyi5.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------

print('Above ikeja 3 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/ikeja?bedrooms=3&added=14&q=for-sale+flats-apartments+lagos+ikeja+3+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("ikeja3.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)




#------------------------------------------------------------------------------------------------------------------------------------


print('Above ikeja 4 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/ikeja?bedrooms=4&added=14&q=for-sale+flats-apartments+lagos+ikeja+4+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("ikeja4.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)


#------------------------------------------------------------------------------------------------------------------------------------

print('Above ikeja 5 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/ikeja?bedrooms=5&added=14&q=for-sale+flats-apartments+lagos+ikeja+5+bedrooms+added+last+30+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("ikeja5.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------

print('Above yaba 3 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/yaba?bedrooms=3&added=14&q=for-sale+flats-apartments+lagos+yaba+3+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("yaba3.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------

print('Above yaba 4 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/yaba?bedrooms=3&added=14&selectedLoc=1&q=for-sale+flats-apartments+lagos+yaba+4+bedrooms+added+last+14+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("yaba4.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)



#------------------------------------------------------------------------------------------------------------------------------------

print('Above yaba 5 bedroom')

for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/yaba?bedrooms=5&added=30&q=for-sale+flats-apartments+lagos+yaba+5+bedrooms+added+last+30+days&page{x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }
    page = requests.get(baseurl)
# print(page)
    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")
    print(len(lists))
    with open("yaba5.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace('₦', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            thewriter.writerow(info)
            # print(info)

