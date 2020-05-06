'''
@Description:  测试将 JSON 文件或是 CSV 文件存入mongoDB 
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-30 10:22:51
@LastEditors: CornC.fcx
@LastEditTime: 2019-06-12 16:44:10
'''

from pymongo import MongoClient
import json

connection = MongoClient('localhost')

db = connection.Test

rcmd = db.nowl_base

file = open('cnki.json', 'r', encoding='utf-8')
datas = json.load(file)
# print(datas)
for each in datas:
    # eachline = json.loads(each)
    print(each)
    rcmd.insert(each)
file.close()