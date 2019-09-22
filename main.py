from bs4 import BeautifulSoup
import urllib.request
import requests
# import os // now useless

def get_info(name):
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
        print(name+'이라는 유저는 없어요!')
        return 0

    source = fp.read()                  
    fp.close()

    soup = BeautifulSoup(source, 'html.parser')
    tbody = soup.find('tbody')
    items = tbody.find_all('tr')

    print(name+'님의 정보입니다.')
    
    for i in items:
        key = i.find('th').get_text(strip = True)
        tmp = i.find('td').get_text().split()
        val = ', '.join(tmp)

        print(key + ': ' + val)



if __name__ == '__main__':
    name = input('누구의 정보를 읽어올까요?\n\
만약 여러 명의 정보를 원하면 쉼표를 이용해 입력해주세요!\n: ')

    name = name.replace(" ","") # no whitespaces
    name = name.split(',') # split by comma
    
    for names in name:
        if names != '':
            get_info(names)
            print('') # new line

    #os.system('pause') 
    input('종료하려면 아무 키나 누르십시오...') # 쉘에서 cmd창 안뜨게
    
