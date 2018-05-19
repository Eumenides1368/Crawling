# -*- coding:utf-8 _*-
import re
tel = '188-8848-8848'
info = re.sub('\D', '', tel)
print(info)