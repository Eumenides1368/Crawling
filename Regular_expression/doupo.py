# -*- coding:utf-8 _*-
# 这小说真的不好看啊
import requests
import re
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/66.0.3359.139 Safari/537.36'
    }

path1 = os.path.abspath('..')
file = open(path1 + '/info/斗破苍穹.txt', 'a+')

def get_info(url):
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        contents = re.findall('<p>(.*?)</p>', req.content.decode('utf-8'), re.S)
        for content in contents:
            print(content)
            file.write(content + '\n')
    else:
        pass

if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2, 20)]
    for url in urls:
        get_info(url)
        time.sleep(1)

file.flush()
file.close()


