# -*- coding:utf-8 _*-
import re
a = 'one1two2three3'
info = re.search('\d+', a)
print(info)
print(info.group())