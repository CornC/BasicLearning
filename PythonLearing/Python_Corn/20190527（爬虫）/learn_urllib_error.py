'''
@Description: Urllib 关于异常处理的部分
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-28 09:37:42
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 10:43:19
'''

'''
首先是 URLError 继承自 OSError 类 是异常模块的基类
    任何 request 所产生的异常都可以通过捕获这个类来进行处理
    reason 属性返回错误原因
'''


# from urllib import request, error

# try:
#     response = request.urlopen('http://127.0.0.1/index.html')
# except error.URLError as e:
#     print(e.reason)


'''
HTTPError 是 URLError 的子类，专用来处理 HTTP 请求错误
    如认证请求失败等，有三个属性：
        code：返回 HTTP 状态码，如404
        reason: 返回错误原因
        headers: 返回请求头
'''


# from urllib import request, error

# try:
#     response = request.urlopen('http://127.0.0.1/jiji.html')
# except error.HTTPError as e:
#     print(e.code, e.reason, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully !')


'''
针对 reason 返回值是对象的情况
'''

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)
except urllib.error.HTTPError as e:
    print(e.code, e.reason, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time Out')