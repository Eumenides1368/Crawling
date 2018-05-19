# -*- coding:utf-8 _*-
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/66.0.3359.139 Safari/537.36'
}

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num ')
    infos = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for rank, info, time in zip(ranks, infos, times):
        if len(info.get_text().split('-')) == 2:
            data = {
                'rank': rank.get_text().strip(),
                'singer': info.get_text().split('-')[0].strip(),
                'song': info.get_text().split('-')[1].strip(),
                'time': time.get_text().strip()
            }
        else:
            continue
        print(data)


if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1, 24)]
    for url in urls:
        get_info(url)
    time.sleep(1)