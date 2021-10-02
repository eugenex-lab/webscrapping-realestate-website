import smtplib
from email.message import EmailMessage

import urllib3

from bs4 import BeautifulSoup
import requests
from csv import  writer

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
for x in range(1,5):

    baseurl = f"https://nigeriapropertycentre.com/for-sale/flats-apartments/lagos/ikoyi/banana-island/showtype?bedrooms=3&page={x}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    }

    page = requests.get(baseurl)
# print(page)



    soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
    lists =  soup.find_all("div",class_="wp-block-content clearfix text-xs-left text-sm-left")

    with open("pythreeal.csv", "w", encoding='utf8' , newline = '') as f:
        thewriter = writer(f)
        header =   ['Property Title','Price','Location','Description']
        thewriter.writerow(header)
        for list in lists:
            title = list.find('h4', class_= "content-title" ).text.replace('\n', '').replace(' \xa0', '')
            price = list.find('span', class_= "pull-sm-left" ).text.replace('\n', '').replace(' \xa0', '')
            add = list.find('address', class_= "voffset-bottom-10" ).text.replace('\n', '').replace(' \xa0', '')
            desc = list.find('div', class_= "description" ).text.replace('\n', '').replace(' \xa0', '')
            info=[title,price,add,desc]
            info = [title]
            thewriter.writerow(info)
            print(info)
print('JUst DO it')
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