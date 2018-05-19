# -*- coding:utf-8 _*-
# 糗事百科段子
import requests
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}

path = os.path.abspath('..')
f = open(path + '/info/糗事百科.txt', 'a+')
infos = []

def judge_sex(class_name):
    if class_name == 'manIcon':
        return '男'
    else:
        return '女'

def get_info(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    for id, level, content, laugh in zip(ids, levels, contents, laughs):
        # print(id, level, content, laugh)
        joke = {
            'id': id,
            'level': level,
            # 'gender': gender,
            'content': content,
            'laugh': laugh
        }
        print(joke)
        infos.append(joke)

if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    for url in urls:
        get_info(url)
    for info in infos:
        print(info)
        try:
            f.write(info['id'] + '\n')
            f.write(info['level'] + '\n')
            # f.write(info['gender'] + '\n')
            f.write(info['content'] + '\n')
            f.write(info['laugh'] + '\n')
        except UnicodeEncodeError:
            pass