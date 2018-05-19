# -*- coding:utf-8 _*-
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/66.0.3359.139 Safari/537.36'
}

res = requests.get('https://book.douban.com/', headers=headers)
html = etree.HTML(res.text)
result = etree.tostring(html)
print(result)