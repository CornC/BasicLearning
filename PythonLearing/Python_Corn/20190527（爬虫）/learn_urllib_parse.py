'''
@Description: 链接解析相关内容
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-28 10:11:39
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-28 11:26:37
'''

'''
urlparse() 此方法可以实现对 URL 的识别和分段

    所以可以得到一个完整的链接的格式：
        scheme://netloc/path;parames?query#fragment

    其 API 如下：
    urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
    
    三个参数的用处分别是：
    
    urlstring: 必填项，待解析的 URL
    scheme：默认协议( http / https ) 在 URL 不包含 Scheme 信息时才生效
            给 URL 添加默认的 Scheme 如果包含则返回解析出的 Scheme信息
    allow_fragments：是否忽略 fragment 
                     False 时 忽略 fragment 即将 fragment 置空
                     其内容会被解析成 path/params/query 的一部分

    ParseResult 实际上是一个元组，可以通过属性名或是索引来获取内容
'''


# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# print(result.scheme, result[0], result[1], result[2], sep='\n')


'''
urlunparse() 是 urlparse() 的对立方法 (构造 URL )
    其传入的参数是一个可迭代的参数，但其长度必须为 6 否则会抛出参数不足异常
'''


# from urllib.parse import urlunparse

# data = ['http', 'www.baidu.com', '/index.html', 'user', 'id=5', 'comment']
# print(urlunparse(data))


'''
urlsplit() 类似于 urlparse() 区别是不在单独解析 params 这一部分
            params 会被合并到 path 中去

urlunsplit() 类似于 urlunparse() 唯一区别是长度必须为 5
'''

'''
urljoin() 同样是生成链接的方法 可以提供一个 base_url （基础链接）作为第一个参数
            将新的链接作为第二个参数，该方法会分析 base_url 的 scheme、netloc 和 path
            并对新连接缺失的地方进行补充

    base_url 提供了三项内容 scheme netloc path 如果这三项在新链接里不存在，则会补充上去
             如果新连接存在，则使用新链接的部分
             而 params query fragment 不起作用
'''

# from urllib.parse import urljoin

# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://corn.com/FAQ.html'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?categroy=2'))

'''
urlencode() 在构造 GET 请求参数是非常有用
'''

# from urllib.parse import urlencode

# params = {
#     'name': 'Corn',
#     'age': 23
# }

# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

'''
parse_qs() 可以反序列化 GET 请求参数 将参数转化成字典

parse_qsl() 同 parse_qs() 只是将参数转化成元组组成的列表
'''

# from urllib.parse import parse_qs

# query = 'name=Corn&age=23'
# print(parse_qs(query))
# print(parse_qsl(query))

'''
quote() 将内容转化为 URL 编码的格式 （防止中文参数的乱码问题）

unquote() 进行 URL 解码 解码（防止中文参数的乱码问题）
'''

from urllib.parse import quote

keyword = '测试'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
