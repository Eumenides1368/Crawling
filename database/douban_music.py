# -*- coding:utf-8 _*-
import requests
from lxml import etree
import re
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
music_top = mydb['music_top']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36'
}

def get_url_music(url):
    html = requests.get(url, headers=headers)
    print(html)
    selector = etree.HTML(html.text)
    music_hrefs = selector.xpath('//a[@class="nbg"]/@href')
    for music_href in music_hrefs:
        get_music(music_href)

def get_music(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    author = re.findall('表演者.*?>(.*?)</a>', html.text, re.S)[0]
    style = re.findall('流派:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(style) == 1:
        this_style = style[0].strip()
    else:
        this_style = '查无此流派'
    time = re.findall('发行时间:</span>&nbsp;(.*?)<br />', html.text, re.S)[0].strip()
    publisher = re.findall('出版者:</span>&nbsp;(.*?)<br />', html.text, re.S)
    if len(publisher) == 0:
        publish = '查无此公司'
    else:
        publish = publisher[0].strip()
    score = selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    print(name, author, this_style, time, publish, score)
    info = {
        'name': name,
        'author': author,
        'style': this_style,
        'time': time,
        'publisher': publish,
        'score':score
    }
    music_top.insert_one(info)

if __name__ == '__main__':
    urls = ['https://music.douban.com/top250?start={}'.format(str(i * 25)) for i in range(0, 10)]
    for url in urls:
        get_url_music(url)
        time.sleep(5)