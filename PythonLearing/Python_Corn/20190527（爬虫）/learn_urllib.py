'''
@Description: 练习爬取python官网
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-27 13:50:58
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-27 14:47:31
'''

'''
练习使用urllib库
'''

import urllib.request

response = urllib.request.urlopen('http://www.python.org')

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(type(response))
print(response.read().decode('UTF-8'))
