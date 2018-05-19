# -*- coding:utf-8 _*-
import re
str = 'xxthexxaaaxxgreekxxdddxxcoffinxxgggxxmysteryxx'
info = re.findall('xx(.*?)xx', str)
print(info)