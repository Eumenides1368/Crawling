# -*- coding:utf-8 _*-
import requests
from lxml import etree
import pymongo
import multiprocessing
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36'
}

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
jianshu = mydb['jianshu']

def get_info(url):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    infos = html.xpath('//div[@class="content"]')
    for info in infos:
        author = info.xpath('div[1]/div/a/text()')[0].strip()
        print('作者：', author)
        time = info.xpath('div[1]/div/span/@data-shared-at')[0]
        print('时间：', time)
        title = info.xpath('a[1]/text()')[0].strip()
        print('标题：', title)
        content = info.xpath('p/text()')[0].strip()
        print('内容：', content)
        view = info.xpath('div[2]/a[1]/text()')[1].strip()
        print('阅读：', view)
        comment = info.xpath('div[2]/a[2]/text()')[1].strip()
        print('评论：', comment)
        # like = info.xpath('div[2]/span[1]/text()')[1].strip()
        # print('喜欢：', like)
        # reward = info.xpath('div[2]/span[2]/text()')[1].strip()
        # print('打赏: ', reward)

if __name__ == '__main__':
    urls = ['https://www.jianshu.com/']
    for url in urls:
        get_info(url)