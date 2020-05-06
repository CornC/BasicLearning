'''
@Description: 从百度学术爬取文献的名称、作者及摘要
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-28 17:32:03
@LastEditors: CornC.fcx
@LastEditTime: 2019-06-05 16:56:38
'''
'''
百度学术的 GET 请求参数格式 :
    第一页： http://xueshu.baidu.com/s?wd=%E5%85%A8%E5%A4%96%E6%98%BE&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D
    第二页： http://xueshu.baidu.com/s?wd=%E5%85%A8%E5%A4%96%E6%98%BE& pn=10 &tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&sc_hit=1
    第三页： http://xueshu.baidu.com/s?wd=%E5%85%A8%E5%A4%96%E6%98%BE& pn=20 &tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&sc_hit=1

    观察可得页数是根据 pn 来判断的，偏移量是 10

    wd = '' 搜索的内容（主题）
    其他固定量（目前来看）
'''

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib import parse
from collections import namedtuple
import requests
import re
import time 
import json

# 获取关键字查询所得列表页面 （一页10个）
def get_list_page(offset):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }

    params = {
        'wd': '全外显',
        'pn': offset,
        'tn': 'SE_baiduxueshu_c1gjeupa',
        'ie': 'utf-8',
        'sc_hit': '1'
    }
    # 代理ip
    proxies = {
        'http': 'http://202.112.237.102:3128',
        'https': 'https://202.112.237.102:3128'
    }
    url = 'http://xueshu.baidu.com/s?' + urlencode(params)  
    # url = 'http://xueshu.baidu.com/s?wd=%E5%85%A8%E5%A4%96%E6%98%BE&tn=SE_baiduxueshu_c1gjeupa&cl=3&bs=%E5%85%A8%E5%A4%96%E6%98%BE&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstAdvancedSearch%7D&sc_from=&sc_as_para='
    print(url)
    response = requests.get(url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        return response.text
    else:
        return None


# 获取文章详细信息页面
def get_info_page(url):

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    # 代理ip
    proxies = {
        'http': 'http://202.112.237.102:3128',
        'https': 'https://202.112.237.102:3128'
    }
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        return None


# 解析页面并获取文章详细内容所在的 url
def get_list_info(text):

    # 论文详细页面网址
    all_paper_urls = []

    soup = BeautifulSoup(text, 'lxml')

    title_list = soup.select('div.sc_content > h3 > a')

    for title in title_list:
        result = {
            'title': title.get_text(),
            'href': title.get('href')
            # 跳转网页： http://xueshu.baidu.com/usercenter/paper/show?paperid=d31c5eb88469b910676f71a7c07efdc8&site=xueshu_se
            # 参数： /s?wd=paperuri % 3A % 28 d31c5eb88469b910676f71a7c07efdc8  % 29 & filter=sc_long_sign&sc_ks_para=q%3D%E5%85%A8%E5%A4%96%E6%98%BE%E5%AD%90%E7%BB%84%E6%B5%8B%E5%BA%8F%E6%8A%80%E6%9C%AF%E5%8F%8A%E5%85%B6%E5%9C%A8%E8%82%BF%E7%98%A4%E7%A0%94%E7%A9%B6%E4%B8%AD%E7%9A%84%E5%BA%94%E7%94%A8&sc_us=4690529917815903308&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8
        }
        patten = str(parse.urlparse(title.get('href')).query).split('&')[0]
        paperid = patten.split('%')[2][2:]
        params = {
            'paperid': paperid,
            'site': 'xueshu_se'
        }
        url = 'http://xueshu.baidu.com/usercenter/paper/show?' + urlencode(params)
        all_paper_urls.append(url)
        print(url)
    print(all_paper_urls)
    return all_paper_urls

# 获得文章详细信息页面中的部分内容
def get_article_info(text):
    # 文章主题（标题）
    title = ''
    # 文章作者
    authors = []
    # 文章摘要
    abstract = ''
    # 关键字
    keywords = []
    # 来源
    source = ''
    # 出版日期
    publish_time = ''
    # 获取免费下载链接
    download_urls = []

    soup = BeautifulSoup(text, 'lxml')
    
    # 标题
    data_title = soup.select_one('h3 > a')
    title = data_title.get_text()
    # 作者
    data_author = soup.select_one('div.author_wr > p.author_text')
    author_list = data_author.find_all('a')
    for item in author_list:
        authors.append(item.get_text())
    # 摘要
    data_abstract = soup.select_one('div.abstract_wr > p.abstract')
    abstract = data_abstract.get_text().replace('  ','').replace('\n','').replace('摘　要：','')
    # 关键字
    data_keywords = soup.select_one('div.kw_wr > p.kw_main')
    if data_keywords:
        words = data_keywords.find_all('a')
        for item in words:
            keywords.append(item.get_text())
    # 来源
    data_source = soup.select_one('div.dtl_journal_container > div.container_right')
    source_info = data_source.find(class_ = 'journal_title')
    if source_info:
        source = source_info.text
    # 出版日期
    publish_time_info = data_source.find(class_ = 'journal_content')
    if publish_time_info:
        publish_time = publish_time_info.text
    # 下载链接
    pattern = soup.find('div', id='savelink_wr')
    if pattern:
        results = pattern.find_all('a')
        for item in results:
            download_urls.append(item.get('href'))
        
    return title, authors, abstract, keywords, source, publish_time, download_urls

# 定义信息存储元组
paper = namedtuple('paper',['title','author','abstract','keywords', 'source', 'publish_time', 'download_urls'])

# 数据放入元组
def set_paper(all_titles,all_authors,all_abstracts,all_keywords,all_sources,all_publishTimes,all_dlUrls):
    papers = [paper(all_titles[i],all_authors[i],all_abstracts[i],all_keywords[i],all_sources[i],all_publishTimes[i],all_dlUrls[i]) for i in range(len(all_titles))]

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
            'download_urls':paper[6],
        }
        json_papers.append(each_data)

    with open('baidu_xueshu.json', 'a', encoding='utf-8') as f:
        for paper in json_papers:
            f.write(json.dumps(paper, ensure_ascii=False) + '\n')

# 程序入口处
if __name__ == "__main__":

    for i in range(0,5):
        print("开始爬取第{}页的内容".format(str(i+1)))
        offset = i * 10
        text = get_list_page(offset)
        all_paper_urls = get_list_info(text)

        all_dlUrls = []
        all_titles = []
        all_authors = []
        all_abstracts = []
        all_keywords = []
        all_sources = []
        all_publishTimes = []
        for page in range(len(all_paper_urls)):
            new_text = get_info_page(all_paper_urls[page])
            time.sleep(5)
            title, authors, abstract, keywords, source, publish_time, download_urls = get_article_info(new_text)

            all_titles.append(title)
            all_authors.append(authors)
            all_abstracts.append(abstract)
            all_keywords.append(keywords)
            all_sources.append(source)
            all_publishTimes.append(publish_time)
            all_dlUrls.append(download_urls)
        
        papers = set_paper(all_titles, all_authors, all_abstracts, all_keywords, all_sources, all_publishTimes, all_dlUrls)
        save_data(papers)
        time.sleep(5)
        
    print('Save Data!')
    # papers = set_paper(all_titles, all_authors, all_abstracts,all_dlUrls)
    # save_data(papers)