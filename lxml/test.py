# -*- coding:utf-8 _*-
import xlwt
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet1')
sheet.write(0, 0, 'python')
sheet.write(1, 1, 'difficult')
book.save('python.xls')
