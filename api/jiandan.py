# -*- coding:utf-8 _*-
import requests
from bs4 import BeautifulSoup
import os

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36'
}

url_path = 'https://www.pexels.com/search/'
word = input('请输入要下载的图: ')
url = url_path + word + '/'

wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')

imgs = soup.select('article > a > img')
lists = []

for img in imgs:
    photo = img.get('src')
    lists.append(photo)

path = os.path.abspath("..") + '/photos/'

for item in lists:
    data = requests.get(item, headers=headers)
    fp = open(path + item.split('?')[0][-10:], 'wb')
    fp.write(data.content)
    fp.close()
