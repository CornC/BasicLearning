'''
@Description: 测试百度身份证识别接口
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-04-26 10:32:17
@LastEditors: CornC.fcx
@LastEditTime: 2020-04-26 10:54:50
'''

import requests
import base64

'''
身份证识别
'''
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=0yRANLtKsq2dWGEvPOuQOGvj&client_secret=BOz8gAxWRSodec1RLRCjrHG7fl9VdwTn'
response = requests.get(host)
if response:
    token = response.json()
    # print(token)
    # print(token['access_token'])
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    f = open('../identityPic/p3.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"id_card_side":"front","image":img}
    access_token = token['access_token']
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

