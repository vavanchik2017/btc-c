# coding: utf-8
import urllib.request
import re
from bs4 import BeautifulSoup
url = "http://bitkurs.ru/"
r = urllib.request.urlopen(url).read().decode('utf-8','ignore')
soup = BeautifulSoup(r, "html.parser")
usd = soup.find('span',{'class': 'usd_c currencies'}).text
rub = soup.find('span',{'class': 'rub_c currencies'}).text
time_msc = soup.find('div',{'class': 'updated_time'}).text
print ("1 BTC=",usd,"=", rub, time_msc)
