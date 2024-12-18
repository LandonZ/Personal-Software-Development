import requests #getting data from website
from bs4 import BeautifulSoup #beautifulsoup for parsing

url = ('https://www.amazon.com/Apple-Bluetooth-Headphones-Personalized-Effortless/dp/B0DGHMNQ5Z/'
       'ref=sr_1_2_sspa?crid=3350YW78O4GMK&dib=eyJ2IjoiMSJ9.z3PTqJjFH4z-EE5L1NErpo2SJto2ojc9UfP'
       '66FrlH4OKKP5EdIlS2pBCVhZOw4pCi65VLnGt9F7Y8JTRQLWDmD9QWtf9r3ZOdf3JKTuAfaU9Jsb_czUuSGxCpc'
       'XHGr1bP98GX3rT18VddNzpTUE1OOL1J6aTV9kloRdWSwNXkYk2BGWn_A8XeAtDVvhx8fi1-PFZQmMDy-T_fKweT'
       'Iz4JIjfKIlXOWBmPZ9CF2Nx18A.EWESTSmXzaVOaK_H7FcDdKUKkabuDJ65e_KlXecg318&dib_tag=se&keywor'
       'ds=airpods&qid=1729978073&sprefix=airpod%2Caps%2C137&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1'
       'zcF9hdGY&psc=1')

#my user agent
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

#now fetch using URL and the headers
page = requests.get(url, headers=headers)
#BeautifulSoup object that parses html
soup = BeautifulSoup(page.content, 'html.parser')

#printing out pretty html code:
print(soup.prettify())

# name of product falls under html id 'productTitle', so use find() method to get the element
# then do get_text() to get the actual name of the title
title = soup.find(id='productTitle')
if title is not None:
    print(title)
else:
    print("Cannot find the HTML element.")