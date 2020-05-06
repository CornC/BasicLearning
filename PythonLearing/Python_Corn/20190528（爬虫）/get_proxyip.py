'''
@Description: 从网上爬取免费的代理ip 并判断是否可用
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-29 09:42:48
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-29 17:37:35
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import json,time,random
import requests

def getheaders():
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers

'''模拟谷歌浏览器访问西刺代理网站，并返回前5页的网页源代码'''
def get_page_source(start_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://' + proxy)
    browser = webdriver.Chrome(chrome_options=chrome_options)   #加入代理
    browser.get(start_url)
    html = browser.page_source  #获取单个网页的源代码
    htmls.append(html)
    time.sleep(5)
    for page in range(1,5):     #获取2-5页的内容
        next_page = browser.find_element_by_class_name('next_page') #获取下一页按钮
        next_page.click()   #点击下一页按钮
        html = browser.page_source
        htmls.append(html)
        time.sleep(5)

'''从网页源代码中获取代理ip'''
def get_http_proxy(htmls):
    for html in htmls:
        soup = BeautifulSoup(html, 'lxml')
        item = soup.find('table')
        trs = item.find_all('tr')
        for tr in trs[1:]:
            http_proxy = {} #把代理ip保存成字典格式
            td = tr.find_all('td')
            http_proxy['ip'] = td[1].text
            http_proxy['port'] = td[2].text
            http_proxy['protocol'] = td[5].text

            if td[5].text == 'HTTPS':   #把HTTP和HTTPS分开保存到两个不同的文件中
                L_https.append(http_proxy)
            else:
                L_http.append(http_proxy)

            ip = td[1].text + ':' + td[2].text
            headers = getheaders()  # 定制请求头
            proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
            response = requests.get('http://www.baidu.com', proxies=proxies, headers=headers).status_code
            if response == 200:
                if td[5].text == 'HTTPS':   #把HTTP和HTTPS分开保存到两个不同的文件中
                    L_https.append(http_proxy)
                else:
                    L_http.append(http_proxy)
            else:
                print("Ip 地址不可用")

'''把HTTP和HTTPS分开保存到两个不同的文件中'''
def save_file():
    file_http = 'http_proxys.json'
    file_https = 'https_proxys.json'
    with open(file_http, 'w', encoding='utf-8') as f:
        f.write(json.dumps(L_http, indent=2))       #indent=2 表示带上缩进，这样json文件比较美观
    with  open(file_https, 'w', encoding='utf-8') as f:
        f.write((json.dumps(L_https, indent=2)))


if __name__ == '__main__':
    htmls = []
    L_http = []
    L_https = []
    proxy = '117.186.214.74:9999'   #这个ip和端口要换成可用的代理ip
    start_url = 'https://www.xicidaili.com/nn/1'    #这个是西刺代理ip官网高匿ip的第一页
    get_page_source(start_url)  #获取网页的源代码
    get_http_proxy(htmls)   #从网页源代码中获取代理ip
    save_file()             #把代理ip保存到json文件
    print('Done！')