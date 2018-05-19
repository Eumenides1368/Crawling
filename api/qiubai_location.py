# -*- coding:utf-8 _*-
import requests
from lxml import etree
import csv
import json
import os

base_path = os.path.abspath('..')
fp = open(base_path + '/info/location.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('address', 'longtitute', 'latitute'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36'
}

def get_user_urls(url):
    url_part = 'https://www.qiushibaike.com/'
    res = requests.get(url_part, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[@class="article block untagged mb15"]')

    for url_info in url_infos:
        user_part_urls = url_info.xpath('div[1]/a[1]/@href')
        if len(user_part_urls) == 1:
            user_part_url = user_part_urls[0]
            get_user_address(url_part + user_part_url)
        else:
            pass

def get_user_address(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    if selector.xpath('//div[2]/div[3]/div[2]/ul/li[4]/text()'):
        address = selector.xpath('//div[2]/div[3]/div[2]/ul/li[4]/text()')
        get_geo(address[0].split(' · '))
    else:
        pass

def get_geo(address):
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    api = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(api, par)
    json_data = json.loads(res.text)
    try:
        geo = json_data['geocodes'][0]['location']
        longtitute = geo.split(',')[0]
        latitite = geo.split(',')[1]
        print(longtitute, latitite)
        writer.writerow((address, longtitute, latitite))
    except IndexError:
        pass

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 5)]
    for url in urls:
        get_user_urls(url)