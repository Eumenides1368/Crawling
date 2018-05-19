# -*- coding:utf-8 _*-
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

url = 'https://www.qiushibaike.com/text/'
res = requests.get(url, headers=headers)
print(res)
selector = etree.HTML(res.text)
print(selector)
# url_infos = selector.xpath('//div[@class="author clearfix"]')
print(url_infos)

for url_info in url_infos:
    id = url_info.xpath('a[2]/h2/text()')[0]
    print(id)