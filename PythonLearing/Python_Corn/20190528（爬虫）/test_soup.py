'''
@Description: 用下载好的 HTML 源码 使用 BeautifulSoup 库解析
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-30 13:55:53
@LastEditors: CornC.fcx
@LastEditTime: 2019-06-17 15:02:37
'''

from bs4 import BeautifulSoup
from urllib import parse
from urllib.parse import urlencode
import re

text = open(
    r'D:\Program Files\LearnPy\PythonPro\Code\20190528（爬虫）\cnki.html',
    'r',
    encoding='utf-8')

htmlhandler = text.read()

soup = BeautifulSoup(htmlhandler, 'lxml')
'''
titile_list = soup.select('div.sc_content > h3 > a')

for title in titile_list:
    result = {
        'title': title.get_text(),
        'href': title.get('href')
        # 跳转网页： http://xueshu.baidu.com/usercenter/paper/show?paperid=d31c5eb88469b910676f71a7c07efdc8&site=xueshu_se
        # 参数： /s?wd=paperuri % 3A % 28 d31c5eb88469b910676f71a7c07efdc8  % 29 & filter=sc_long_sign&sc_ks_para=q%3D%E5%85%A8%E5%A4%96%E6%98%BE%E5%AD%90%E7%BB%84%E6%B5%8B%E5%BA%8F%E6%8A%80%E6%9C%AF%E5%8F%8A%E5%85%B6%E5%9C%A8%E8%82%BF%E7%98%A4%E7%A0%94%E7%A9%B6%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8&sc_us=4690529917815903308&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8
    }

    wd = str(parse.urlparse(title.get('href')).query).split('&')[0]
    paperid = wd.split('%')[2][2:]
    print(paperid)


    # print(result)
# print(soup.select('div.sc_content > h3 > a'))
# print(soup.find_all('div', 'sc_info'))
'''
'''
title = soup.select_one('h3 > a')
title_text = title.get_text()

author = soup.select_one('div.author_wr > p.author_text')
author_list = author.find_all('a')
authors = []
for item in author_list:
    authors.append(item.get_text())

abstract = soup.select_one('div.abstract_wr > p.abstract')
text = abstract.get_text().replace(' ','').replace('\n','').replace('摘　要：','')


key = soup.select_one('div.kw_wr > p.kw_main')
words = key.find_all('a')
keywords = []
for item in words:
    keywords.append(item.get_text()) 

print(text)
# print(text)
'''
###########################################################
# title_list = soup.select('div.wz_content > h3 > a')
# links = []
# downloads = []
# for title in title_list:
#     link = title.get('href')
#     if link.find('Article') > 0:
#         links.append(link)
#     else:
#         downloads.append(link)

# data = soup.select('span.year-count > span')

# sources = []
# datetime = []
# types = []
# for index in range(len(links)):
#     if data[index*2].get('title') != None:

#         sourcestr = data[index*2].text
#         sourcelist = sourcestr.split('\xa0')
#         # print(sourcelist)
#         if links[index].find('CPFD') > 0:
#             artype = 'CPFD'
#             date = sourcestr[-10:]
#         elif links[index].find('CJFD') > 0:
#             artype = 'CJFD'
#             date = sourcestr[-10:]
#         else:
#             artype = 'CDMD'
#             date = sourcestr[-5:]
        
#         types.append(artype)
#         sources.append(sourcelist[0])
#         datetime.append(date)

# print(downloads)
# print(links)
# print(types)
# print(sources)
# print(datetime)
# print(len(downloads))
# print(len(links))
# print(len(types))
# print(len(sources))
# print(len(datetime))
####################################################

title_data = soup.find('h1.xx_title')
title = title_data.text

print(title)
# data = soup.find('div', style="text-align:center; width:740px; height:30px;")
# userlist = data.find_all('a')

# mylist = []
# for item in userlist:
#     mylist.append(item.text)

# mydata = soup.find('div', style="text-align:left;word-break:break-all")
# abstarct = mydata.text.replace('  ','').replace('\n','')

# hapdata = soup.find_all('meta')
# keywords = []

# for item in hapdata:
#     if item.get('name') == 'autoKeywords':
#         keys = item.get('content')
#         if keys.find(';') > 0:
#             # print('1')
#             keylist = keys.split(';')
#         else:
#             keylist = keys.split(' ')
        
#         for key in keylist:
#             keywords.append(key)

# print(title)
# print(mylist)
# print(abstarct)
# print(keywords)

###################################################
# print('downloads ')
# print(downloads)
# # 文章主题（标题）
# title = ''
# # 文章作者
# authors = []
# # 文章摘要
# abstract = ''
# # 获取免费下载链接
# download_urls = []
# # 关键字
# keywords = []

# # 标题
# data_title = soup.select_one('h3 > a')
# title = data_title.get_text()
# # 作者
# data_author = soup.select_one('div.author_wr > p.author_text')
# author_list = data_author.find_all('a')
# for item in author_list:
#     authors.append(item.get_text())
# # 摘要
# data_abstract = soup.select_one('div.abstract_wr > p.abstract')
# abstract = data_abstract.get_text().replace(' ','').replace('\n','').replace('摘　要：','')
# # 关键字
# data_keywords = soup.select_one('div.kw_wr > p.kw_main')
# words = data_keywords.find_all('a')
# for item in words:
#     keywords.append(item.get_text())
# # 下载链接
# data = ''
# pattern = soup.find('div',id="allversion_wr")
# spans = pattern.find()
# if pattern:
#     print('aaaa')
#     results = pattern.find_all('a')
#     links = []
#     for item in results:
#         links.append(item.get('href'))
#     for link in links:
#         if link.find('cnki') > 0:
#             data = link     
# print(data)
# 摘要
# data_abstract = soup.select_one('div.abstract_wr > p.abstract')
# abstract = data_abstract.get_text().replace('  ','').replace('\n','').replace('摘　要：','')
# print(abstract)
# data_source = soup.select_one('div.dtl_journal_container > div.container_right')
# data_info = data_source.find(class_ = 'journal_title')
# if data_info:
#     data = data_info.text
# print(data)
# source = data
# publishTime = data_source.find('div').get('title')
#     for item in results:
#         data.append(item.get('href')
        # # each_authors = []
        # each_source = ''
        # alist=span.find('span','sc_time')
        # each_source=alist
        # all_authors.append(each_source)

# all_authors=[]

# author_datas = soup.find_all('div','sc_info')

# for authors in author_datas:#authors类型为<class 'bs4.element.Tag'>
#     # for span in authors.find_all('span'):#此时span类型为<class 'bs4.element.Tag'>
#     for span in authors.find_all('span'):

#         print(span)
# results = re.findall(pattern,text)

# for item in results:
#     each_data = {
#         'url':item[0],
#         'download':item[1]
#     }
#     if "免费" in each_data.get('download'):
#         download_urls.append(each_data.get('url'))
#         # print(each_data)
# print(title)
# print(authors)
# print(abstract)
# print(download_urls)
# print(data)

# 论文详细页面网址
# all_paper_urls = []

# title_list = soup.select('div.sc_content > h3 > a')

# for title in title_list:

#     result = {
#         'title': title.get_text(),
#         'href': title.get('href')
#         # 跳转网页： http://xueshu.baidu.com/usercenter/paper/show?paperid=d31c5eb88469b910676f71a7c07efdc8&site=xueshu_se
#         # 参数： /s?wd=paperuri % 3A % 28 d31c5eb88469b910676f71a7c07efdc8  % 29 & filter=sc_long_sign&sc_ks_para=q%3D%E5%85%A8%E5%A4%96%E6%98%BE%E5%AD%90%E7%BB%84%E6%B5%8B%E5%BA%8F%E6%8A%80%E6%9C%AF%E5%8F%8A%E5%85%B6%E5%9C%A8%E8%82%BF%E7%98%A4%E7%A0%94%E7%A9%B6%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8&sc_us=4690529917815903308&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8
#     }
#     patten = str(parse.urlparse(title.get('href')).query).split('&')[0]
#     paperid = patten.split('%')[2][2:]
#     params = {
#         'paperid': paperid,
#         'site': 'xueshu_se'
#     }
#     url = 'http://xueshu.baidu.com/usercenter/paper/show?' + urlencode(params)
#     all_paper_urls.append(url)

# params2 = {
#     'wd': '全外显',
#     'pn': 20,
#     'tn': 'SE_baiduxueshu_c1gjeupa',
#     'ie': 'utf-8',
#     'sc_hit': '1'
# }
# url2 = "http://xueshu.baidu.com/s?" + urlencode(params2)
