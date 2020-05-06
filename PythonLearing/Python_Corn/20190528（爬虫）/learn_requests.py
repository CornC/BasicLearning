'''
@Description: 相较于 urllib 库， request 库更加方便
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-28 13:47:27
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 17:24:39
'''

'''
urllib 库中的 urlopen() 方法实际上就是通过 GET 方式请求网页
在 requests 库中就是 get() 方法
'''

'''
import requests

#加入参数
data = {
    'name': 'A',
    'age': 23
}

#r = requests.get('https://httpbin.org/get', params=data)
#r = requests.post('http://httpbin.org/post')
#r = requests.put('http://httpbin.org/put')
#r = requests.delete('http://httpbin.org/delete')
#r = requests.head('http://httpbin.org/get')
#r = requests.options('http://httpbin.org/get')

print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.json())
print(type(r.json()))
print(r.cookies)
'''

'''
举个栗子
'''

# import requests
# import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

'''
抓取二进制数据
'''

'''
import requests

data = {
    'name': 'corn',
    'age': 23
}

r = requests.get('https://github.com/favicon.ico')
response = requests.post('http://httpbin.org/post', data=data)
print(response.text)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
# print(r.text)
# print(r.content)
'''

'''
上传文件
'''

# import requests

# files = {
#     'file': open('favicon.ico', 'rb')
# }

# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

'''
获取 Cookies
'''

# import requests

# r = requests.get('http://www.baidu.com')
# print(r.cookies)

# for key, value in r.cookies.items():
#     print(key + '=' + value)

'''
使用 Cookies
'''


import requests

# 利用构造 RequestsCookieJar 对象来设置 cookies
# cookies = 'd_c0="AMBhTK3Xqg2PTmnw9Bpm7O84R3aT1_hI3NQ=|1527583344"; _zap=a440e6a0-2358-43a1-bf84-e47e802925b6; __gads=ID=d5c6a31711ce606f:T=1557575552:S=ALNI_Mb5K2Y6t1y0t3hijPc11AKhSTTf9Q; l_n_c=1; q_c1=40c6fcc7bf00460e9d0ee56cc7eac365|1559024348000|1527583344000; _xsrf=ec942f72ca5fb01afc4843afe53d743b; n_c=1; __utmc=51854390; _xsrf=eZM9BmAppApo0gGdbCoh4ka0DLrHIX15; tgw_l7_route=578107ff0d4b4f191be329db6089ff48; l_cap_id="ZDhmNWZmZGQ5OTc0NDViOWE4YzE3ZTM2N2ZiYjU5Y2I=|1559027926|d9570bd2fb49de698cd7981c8afde27b72922cf5"; r_cap_id="NjQyNDFjZDIxN2VlNGVhNGI5Zjk2MWE3NDE2NDFiZTU=|1559027926|09d48f21ca2d830d1dfafbaedb5aaa2368b8b765"; cap_id="MDQxZjYwMjBmZTViNGYzNzgxOGQ3MmFmNzY3ZWVmNDE=|1559027926|2ee1f17ce66a45c62033b886a7a579296607c3f3"; capsion_ticket="2|1:0|10:1559028137|14:capsion_ticket|44:OTcyNmZhNWM1NGUyNGZiZmI3YjNiMWM1ZGM1ZmY5NjU=|138684fbf5848891ea3109d927077ee7199e4fa85a2975e615262e2f5b2f15cf"; z_c0="2|1:0|10:1559028179|4:z_c0|92:Mi4xM3RMeER3QUFBQUFBd0dGTXJkZXFEU1lBQUFCZ0FsVk4weV9hWFFETVB6X25HVFRBLU9UX1NYeXo5dmEwSkFKemZn|570c25afa15e7aa1f49ae23d1bba6e0fb3baa7253f26d638915ca35f28b1f98c"; __utma=51854390.1325872933.1559024351.1559024351.1559028182.2; __utmb=51854390.0.10.1559028182; __utmz=51854390.1559028182.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signup; __utmv=51854390.100--|2=registration_date=20190528=1^3=entry_date=20180529=1'
# jar = requests.cookies.RequestsCookieJar()

# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
# }

# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)

headers = {
    # 'Cookie': 'd_c0="AMBhTK3Xqg2PTmnw9Bpm7O84R3aT1_hI3NQ=|1527583344"; _zap=a440e6a0-2358-43a1-bf84-e47e802925b6; __gads=ID=d5c6a31711ce606f:T=1557575552:S=ALNI_Mb5K2Y6t1y0t3hijPc11AKhSTTf9Q; l_n_c=1; q_c1=40c6fcc7bf00460e9d0ee56cc7eac365|1559024348000|1527583344000; _xsrf=ec942f72ca5fb01afc4843afe53d743b; n_c=1; __utmc=51854390; _xsrf=eZM9BmAppApo0gGdbCoh4ka0DLrHIX15; tgw_l7_route=578107ff0d4b4f191be329db6089ff48; l_cap_id="ZDhmNWZmZGQ5OTc0NDViOWE4YzE3ZTM2N2ZiYjU5Y2I=|1559027926|d9570bd2fb49de698cd7981c8afde27b72922cf5"; r_cap_id="NjQyNDFjZDIxN2VlNGVhNGI5Zjk2MWE3NDE2NDFiZTU=|1559027926|09d48f21ca2d830d1dfafbaedb5aaa2368b8b765"; cap_id="MDQxZjYwMjBmZTViNGYzNzgxOGQ3MmFmNzY3ZWVmNDE=|1559027926|2ee1f17ce66a45c62033b886a7a579296607c3f3"; capsion_ticket="2|1:0|10:1559028137|14:capsion_ticket|44:OTcyNmZhNWM1NGUyNGZiZmI3YjNiMWM1ZGM1ZmY5NjU=|138684fbf5848891ea3109d927077ee7199e4fa85a2975e615262e2f5b2f15cf"; z_c0="2|1:0|10:1559028179|4:z_c0|92:Mi4xM3RMeER3QUFBQUFBd0dGTXJkZXFEU1lBQUFCZ0FsVk4weV9hWFFETVB6X25HVFRBLU9UX1NYeXo5dmEwSkFKemZn|570c25afa15e7aa1f49ae23d1bba6e0fb3baa7253f26d638915ca35f28b1f98c"; __utma=51854390.1325872933.1559024351.1559024351.1559028182.2; __utmb=51854390.0.10.1559028182; __utmz=51854390.1559028182.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signup; __utmv=51854390.100--|2=registration_date=20190528=1^3=entry_date=20180529=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
r = requests.get('http://xueshu.baidu.com/', headers=headers)
#r = requests.get('https://www.zhihu.com', headers=headers, cookies=jar)
print(r.text)


'''
使用 Session
'''

'''
import requests

# 未使用 Session 无法获取 Session
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')

# 使用 Session 可以获取到 （模拟同一个会话）
s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)
'''

'''
SSL 证书验证
'''

'''
import requests
#import logging
#from requests.packages import urllib3 

# 设置忽略警告
#urllib3.disable_warnings()

# 捕获警告到日志
#logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
'''

'''
通过 url data headers 构造一个 Request 对象，在调用 Session 的 prepare_request()方法
    将其转换成一个 Prepared Request 对象，然后调用 send() 方法发送即可
'''

# from requests import Request, Session

# url = 'http://httpbin.org/post'
# data = {
#     'name': 'Corn',
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
# }

# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prpped = s.prepare_request(req)
# r = s.send(prpped)
# print(r.text)