# -*- coding:utf-8 _*-
import pymongo
client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
test = mydb['test']
test.insert_one({'name': 'Jan', 'sex': 'male', 'grade':88})