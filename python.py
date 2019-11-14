from urllib.request import urlopen
from bs4 import BeautifulSoup


quote_page = 'https://www.anwalt.de/konto/start'

page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup

name = name_box.text.strip() 
print ('name')

# price_box = soup.find('div', attrs={'span[class*="priceText__1853e8a5"]'})
# price = price_box.text
# print ('price')

print(name_box)


# import requests
# import urllib.request
# import time
# from bs4 import BeautifulSoup

# url = 'http://web.mta.info/developers/turnstile.html'
# response = requests.get(url)