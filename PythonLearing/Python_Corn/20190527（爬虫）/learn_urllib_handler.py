'''
@Description: 构造更加完整和高级的 Header 要使用到 Handler
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-27 15:53:55
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 09:34:33
'''

'''
代理的使用
'''

'''
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://210.77.24.224:1080',
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
'''

'''
urllib.request 模块里的 BaseHandler 类是其他所有 Handler 类的父类，提供最基本的方法

常用到的子类有：
    HTTPDefaultErrorHandler : 用于处理 HTTP 响应错误，抛出 HTTPError 类型的异常
    HTTPRedirectHandler : 用于处理重定向
    HTTPCookieProcessor : 用于处理 Cookies 
    ProxyHandler : 用于设置代理，默认代理为空
    HTTPPasswordMgr : 用于管理密码，维护了用户名和密码的表
    HTTPBasicAuthHandler : 用于管理认证，可以解决认证问题

另一个重要的类就是 OpenerDirector 这就是 urllib 提供的一个 Opener
    Opener 可以使用 Open() 方法，返回值同 urlopen()

所以需要用 Handler 去构建 Opener
'''

'''
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:3000/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
'''

'''
MozillaCookieJar 是 CookieJar 的子类，用来处理 Cookie 和文件相关的事件

LWPCookieJar 同样可以，只是保存的格式不同 会保存成 libwww-perl (LWP) 格式
'''


import http.cookiejar
import urllib.request
# 将cookie 存入文件

###
#filename = 'Mozilla_cookies.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)
#cookie = http.cookiejar.LWPCookieJar(filename)
###
cookie = http.cookiejar.LWPCookieJar()
cookie.load('LWP_cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

print(response.read().decode('utf-8'))
### 存入
#cookie.save(ignore_discard=True, ignore_expires=True)
###

# for item in cookie:
#     print(item.name + '=' + item.value)
