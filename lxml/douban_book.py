# -*- coding:utf-8 _*-
from lxml import etree
import requests
import csv
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

path = os.path.abspath('..')
f = open(path + '/info/douban_book.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]

for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else '空'
        writer.writerow((name, url, author, publisher, date, price, rate, comment))
        print(name, url, author, publisher, date, price, rate, comment)
f.close()