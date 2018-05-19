# -*- coding:utf-8 _*-
from lxml import etree
html = etree.parse('flower.html')
result = etree.tostring(html, pretty_print=True)
print(result)
