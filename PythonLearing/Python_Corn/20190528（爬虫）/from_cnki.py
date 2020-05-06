'''
@Description: 对于知网知识搜索的爬虫
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-06-11 11:19:22
@LastEditors: CornC.fcx
@LastEditTime: 2019-06-19 17:42:31
'''

'''
主页是 http://search.cnki.com.cn/default.aspx

没有看到请求（假设搜索 abc ） 跳转页面为 http://search.cnki.com.cn/Search.aspx?q=abc
可以看到搜索跳转需要的参数只有 Search.apsx?p=搜索词
                    翻页操作    第二页 http://search.cnki.com.cn/Search.aspx?q=abc&rank=relevant&cluster=all&val=&p=15
                    翻页操作    第三页 http://search.cnki.com.cn/Search.aspx?q=abc&rank=relevant&cluster=all&val=&p=30
偏移量为15 即一页 15 条数据

知网搜索的页面右侧有文献的类型筛选 包括（搜索的abc）
                                    全部文章    http://search.cnki.com.cn/search.aspx?q=abc&rank=relevant&cluster=zyk&val=
                                    学术期刊    http://search.cnki.com.cn/search.aspx?q=abc&rank=relevant&cluster=zyk&val=CJFDTOTAL
                                    博士论文    http://search.cnki.com.cn/search.aspx?q=abc&rank=relevant&cluster=zyk&val=CDFDTOTAL
                                    硕士论文    http://search.cnki.com.cn/search.aspx?q=abc&rank=relevant&cluster=zyk&val=CMFDTOTAL
                                    会议论文    http://search.cnki.com.cn/search.aspx?q=abc&rank=relevant&cluster=zyk&val=CPFDTOTAL

                                    CPFD 会议
                                    CDMD 硕博
                                    CJFD 期刊

还有学科分类（是否爬取？）

尝试爬一下

'''

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib import parse
from collections import namedtuple
import random
import requests
import re
import time 
import json

# 获取关键字查询所得列表页面 （一页15个）
def get_list_page(word, offset):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }

    params = {
        'q': word,
        'p': offset,
        'rank': 'relevant',
        'cluster': 'all',
        'val' : '',
    }
    # 代理ip
    proxies = {
        'http': 'http://202.112.237.102:3128',
        'https': 'https://202.112.237.102:3128'
    }
    url = 'http://search.cnki.com.cn/Search.aspx?' + urlencode(params)  
    # url = 'http://xueshu.baidu.com/s?wd=%E5%85%A8%E5%A4%96%E6%98%BE&tn=SE_baiduxueshu_c1gjeupa&cl=3&bs=%E5%85%A8%E5%A4%96%E6%98%BE&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D&sc_from=&sc_as_para='
    # print(url)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    else:
        return None

# 解析页面并获取文章详细内容所在的 url
def get_list_info(text):

    # 论文详细页面网址
    all_paper_urls = []
    # 获取下载链接
    download_urls = []
    # 文章的来源
    all_paper_sources = []
    # 文章的出版日期（或期刊期数）
    all_paper_publish = []
    # 文章的类别
    all_paper_types = []

    soup = BeautifulSoup(text, 'lxml')

    # 获取链接（下载和详细页）
    title_list = soup.select('div.wz_content > h3 > a')

    for title in title_list:
        link = title.get('href')
        # 由于头里包着两个a标签 只能通过便签内信息进行区分
        if link.find('Article') > 0:
            all_paper_urls.append(link)
        else:
            download_urls.append(link)

    paper_info_list = soup.select('span.year-count > span')

    for index in range(len(all_paper_urls)):
        if paper_info_list[index*2].get('title') != None:

            sourcestr = paper_info_list[index*2].text
            sourcelist = sourcestr.split('\xa0')
            # print(sourcelist)
            if all_paper_urls[index].find('CPFD') > 0:
                artype = 'CPFD'
                date = sourcestr[-10:]
            elif all_paper_urls[index].find('CJFD') > 0:
                artype = 'CJFD'
                date = sourcestr[-10:]
            else:
                artype = 'CDMD'
                date = sourcestr[-5:]
        
        all_paper_types.append(artype)
        all_paper_sources.append(sourcelist[0])
        all_paper_publish.append(date)
    print(all_paper_urls)
    return all_paper_urls, all_paper_sources, all_paper_types, all_paper_publish, download_urls

# 获取文章详细信息页面
def get_info_page(url):
    maxTryNum = 20
    for tries in range(maxTryNum):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
            }
            # 代理ip
            proxies = {
                'http': 'http://202.112.237.102:3128',
                'https': 'https://202.112.237.102:3128'
            }
            response = requests.get(url, headers=headers, timeout=60)
            print(response.status_code + 22)
            if response.status_code == 200:
                return response.text
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                print("Has tried %d times to access url %s, all failed!" % (maxTryNum, url))
                return "FalseToOpenUrl"

# 获得文章详细信息页面中的部分内容
def get_article_info(text):

    # 文章标题
    title = ''
    # 文章作者
    authors = []
    # 文章摘要
    abstract = ''
    # 关键字
    keywords = []

    soup = BeautifulSoup(text, 'lxml')
    

    # 标题
    title_data = soup.select_one('h1.xx_title')
    title = title_data.text
    # 作者
    data_author = soup.find('div', style="text-align:center; width:740px; height:30px;")
    userlist = data_author.find_all('a')

    for item in userlist:
        authors.append(item.text)
    # 摘要
    data_abstract = soup.find('div', style="text-align:left;word-break:break-all")
    abstract = data_abstract.text.replace('  ','').replace('\n','').replace('\r','')

    data_keywords = soup.find_all('meta')

    for item in data_keywords:
        if item.get('name') == 'keywords':
            keys = item.get('content')
            if keys.find(';') > 0:
                # print('1')
                keylist = keys.split(';')
            else:
                keylist = keys.split(' ')
            
            for key in keylist:
                keywords.append(key)

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
    # abstract = data_abstract.get_text().replace('  ','').replace('\n','').replace('摘　要：','')
    # # 关键字
    # data_keywords = soup.select_one('div.kw_wr > p.kw_main')
    # if data_keywords:
    #     words = data_keywords.find_all('a')
    #     for item in words:
    #         keywords.append(item.get_text())
    # # 来源
    # data_source = soup.select_one('div.dtl_journal_container > div.container_right')
    # source_info = data_source.find(class_ = 'journal_title')
    # if source_info:
    #     source = source_info.text
    # # 出版日期
    # publish_time_info = data_source.find(class_ = 'journal_content')
    # if publish_time_info:
    #     publish_time = publish_time_info.text
    # # 下载链接
    # pattern = soup.find('div', id='savelink_wr')
    # if pattern:
    #     results = pattern.find_all('a')
    #     for item in results:
    #         download_urls.append(item.get('href'))
        
    return title, authors, abstract, keywords

# 定义信息存储元组
paper = namedtuple('paper',['title','author','abstract','keywords', 'source', 'publish_time', 'type', 'download_urls'])

# 数据放入元组
def set_paper(all_titles, all_authors, all_abstracts, all_keywords, all_paper_sources, all_paper_publish, all_paper_types, download_urls):
    papers = [paper(all_titles[i],all_authors[i],all_abstracts[i],all_keywords[i],all_paper_sources[i],all_paper_publish[i],all_paper_types[i],download_urls[i]) for i in range(len(all_titles))]

    return papers

#将文献主题、作者、摘要、下载路径转换成字典保存，使用json进行存储
def save_data(papers):
    json_papers = []
    for paper in papers:
        each_data = {
            'Title':paper[0],
            'Author':paper[1],
            'Abstract':paper[2],
            'Keywords':paper[3],
            'Source':paper[4],
            'PublishTime':paper[5],
            'ArticleType':paper[6],
            'DownloadUrl':paper[7],
        }
        json_papers.append(each_data)

    with open('cnki.txt', 'a', encoding='utf-8') as f:
        for paper in json_papers:
            f.write(json.dumps(paper, ensure_ascii=False) + ',\n')
                
# 程序入口处
if __name__ == "__main__":
    
    for i in range(11,20):
        print("开始爬取第{}页的内容".format(str(i+1)))
        offset = i * 15
        text = get_list_page('妇科感染', offset)
        all_paper_urls, all_paper_sources, all_paper_types, all_paper_publish, download_urls = get_list_info(text)
        # all_paper_urls = get_list_info(text)

        # all_dlUrls = []
        all_titles = []
        all_authors = []
        all_abstracts = []
        all_keywords = []
        # all_sources = []
        # all_publishTimes = []
        for i in range(len(all_paper_urls)):
            new_text = get_info_page(all_paper_urls[i])
            if new_text == "FalseToOpenUrl":
                print("Skip !")
                continue

            time.sleep(random.randint(20,40))
            title, authors, abstract, keywords = get_article_info(new_text)

            all_titles.append(title)
            all_authors.append(authors)
            all_abstracts.append(abstract)
            all_keywords.append(keywords)
        #     all_sources.append(source)
        #     all_publishTimes.append(publish_time)
        #     all_dlUrls.append(download_urls)
        
        print(len(all_titles))
        print(len(all_authors))
        print(len(all_abstracts))
        print(len(all_keywords))
        print(len(all_paper_urls))
        print(len(all_paper_sources))
        print(len(all_paper_types))
        print(len(all_paper_publish))
        print(len(download_urls))

        papers = set_paper(all_titles, all_authors, all_abstracts, all_keywords, all_paper_sources, all_paper_publish, all_paper_types, download_urls)
        save_data(papers)
        time.sleep(random.randint(10,30))
        
    print("Save Data! ")
