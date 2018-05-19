# -*- coding:utf-8 _*-
import requests
from lxml import etree
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/66.0.3359.139 Safari/537.36'
}

problems = []

url = 'http://acmoj.shu.edu.cn/contest/32/problems/'
req = requests.head(url, headers=headers)
selector = etree.HTML(req.text)
print(req)