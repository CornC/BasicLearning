'''
@Description: Urllib 库的 Request 方法
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-27 15:23:31
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 10:43:48
'''

'''
urlopen 可以实现最基本的请求，但无法自定义 header 等参数 需要使用 Request 类
'''

'''
urllib.request.Request(url, data=None, headers={}, origin_req_host=None,
                        unverifiable=False, method=None)

其中 url 为必须参数，其它为可选参数

data 同 urlopen 方法，必须是字节流。如果是字典使用 urllib.parse.urlencode()
headers 是一个字典，就是请求头，可以直接构造 header 参数
                            也可以调用请求实例的 add_header()方法添加
（主要是为了修改 User-Agent 来模拟浏览器请求）
origin_req_host 指请求方的 host 地址或是 ip 地址
unverifiable 表示这个请求是无法验证的，默认 False 即无权限
method 表示请求的方法 如 GET POST PUT 等
'''


# import urllib.request

# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)

# print(response.read().decode('utf-8'))


from urllib import request, parse

url = 'http://httpbin.org/post'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)',
#     'Host': 'httpbin.org'
# }

dict = {
    'name': 'Corn'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, method='POST')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64)')
response = request.urlopen(req)

print(response.read().decode('utf-8'))