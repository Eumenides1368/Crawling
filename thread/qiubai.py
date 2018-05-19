# -*- coding:utf-8 _*-
import requests
import re
import time
from multiprocessing import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36'
}

def crawling(url):
    res = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(.*?)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论', res.text, re.S)
    # for id, content, laugh, comment in zip(ids, contents, laughs, comments):
    #     print(id, content, laugh, comment)

if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 5)]
    start_1 = time.time()
    for url in urls:
        crawling(url)
    end_1 = time.time()
    print('串行：', end_1 - start_1)

    start_2 = time.time()
    pool = Pool(processes=2)
    pool.map(crawling, urls)
    end_2 = time.time()
    print('并行2进程：', end_2 - start_2)

    start_3 = time.time()
    pool = Pool(processes=4)
    pool.map(crawling, urls)
    end_3 = time.time()
    print('并行4进程：', end_3 - start_3)