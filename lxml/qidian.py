# -*- coding:utf-8 _*-
import xlwt
import requests
from lxml import etree
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/66.0.3359.139 Safari/537.36'
}

info_lists = []

def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)

    single_books = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for single_book in single_books:
        name = single_book.xpath('div[2]/h4/a/text()')[0]
        author = single_book.xpath('div[2]/p[1]/a[1]/text()')[0]
        big_style = single_book.xpath('div[2]/p[1]/a[2]/text()')[0]
        small_style = single_book.xpath('div[2]/p[1]/a[3]/text()')[0]
        state = single_book.xpath('div[2]/p[1]/span/text()')[0]
        intro = single_book.xpath('div[2]/p[2]/text()')[0].strip()
        word = single_book.xpath('div[2]/p[3]/span/span/text()')[0].strip('万字')

        info_list = [name, author, big_style, small_style, state, intro, word]
        print(info_list)
        info_lists.append(info_list)

    time.sleep(1)

if __name__ == '__main__':
    urls = ['https://www.qidian.com/all/?page={}'.format(str(i)) for i in range(1, 11)]
    for url in urls:
        get_info(url)

    head = ['name', 'author', 'big_style', 'small_style', 'state', 'intro', 'word']
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('Sheet')
    for l in range(0, len(head)):
        sheet.write(0, l, head[l])

    i = 0
    for info_list in info_lists:
        i += 1
        j = 0
        for info in info_list:
            sheet.write(i, j, info)
            j += 1

    book.save('qidian.xls')





