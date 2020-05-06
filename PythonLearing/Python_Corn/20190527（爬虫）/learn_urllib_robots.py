'''
@Description: Robots 协议的相关内容
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-28 11:26:52
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 11:59:08
'''

'''
Robots 协议也称作爬虫协议 通常是一个在网站根目录下叫做 robots.txt 的文本文件
    该文件定义了爬虫允许爬取的范围
    通常有三个字段

    User-Agent: 规定了搜索爬虫的名称 *表示对任何爬虫有效
    Disallow: 禁止爬取的目录 为空时表示全部可以爬取
    Allow：可以爬取的目录

robotparser 模块是用来解析 robots.txt 文件的模块，
    它提供了一个类：
        RobotFileParser, 它可以根据网站的 robots.txt 来判断是否有权限爬取网页

RobotFileParser 常用的几个方法：
    seturl(): 用来设置 robots.txt 的链接，如创建对象时就传入了则无需此方法
    read(): 读取 robots.txt 并分析，不返回任何内容，但执行读取操作
    parse(): 解析 robots.txt 文件
    can_fetch(): 传入两个参数，第一个是 User-Agent ，第二个就是要抓取的 URL
                    返回内容是能否抓取这个 URL （True or False）
    mtime(): 返回上次抓取和分析 robots.txt 文件的时间 （可能需要定期去抓取）
    modified(): 将当前时间设置为上次抓取和分析 robots.txt 的时间
'''

from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
#rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/7220302b22e6'))
print(rp.can_fetch('*', 'http://www.jianshu.com/serach?q=python&page=1&type=collections'))

