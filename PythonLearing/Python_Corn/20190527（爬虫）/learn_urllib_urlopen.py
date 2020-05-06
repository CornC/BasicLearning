'''
@Description: 
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-27 14:26:24
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 10:44:02
'''

'''
urllib.request.urlopen(url, data = None, [timeout,]*, 
                        cafile = None,capath = None,
                        cadefault = False, context = None)

data 参数：
    可选参数，如果有则需要通过 bytes() 转化成字节流编码。
    如果 data 参数存在，则使用 post 方法
'''

# import urllib.request
# import urllib.parse

# data = bytes(urllib.parse.urlencode({'word' : 'hello '}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

'''
超时参数 timeout
    请求超过该时间就会抛出异常
'''

import socket
import urllib.error

# resp = urllib.request.urlopen('http://httpbin.org', timeout=100)

try:
    resp = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')

'''
Context 参数
    必须是 ssl.SSLContext 类型，用来指定 SSL 设置（安全设置）
'''

'''
cafile 和 capath 两个参数分别指定 CA 证书和路径（请求 HTTPS 链接）

cadefault 已启用  默认为 False
'''
