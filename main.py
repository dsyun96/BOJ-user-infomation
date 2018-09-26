from bs4 import BeautifulSoup
import urllib.request
import requests
import sys

name = input('누구의 정보를 읽어올까요? ')
url = 'https://www.acmicpc.net/user/' + name

# infomation of browser
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
hds = { 'User-Agent' : user_agent }

req = urllib.request.Request(url, headers = hds)
temp = 0
fp = None
while temp < 10:
    try:
        fp = urllib.request.urlopen(req, timeout = 10)
        break
    except:
        temp += 1

if fp == None:
    print('그런 유저는 없어요!')
    exit(0)

source = fp.read()
fp.close()

soup = BeautifulSoup(source, 'html.parser')
tbody = soup.find('tbody')
items = tbody.find_all('tr')

for i in items:
    key = i.find('th').get_text(strip = True)
    tmp = i.find('td').get_text().split()
    val = ', '.join(tmp)

    print(key + ': ' + val)