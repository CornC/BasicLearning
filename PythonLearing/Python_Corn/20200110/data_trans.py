'''
@Description: 数据转置
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2020-01-13 14:29:00
@LastEditors: CornC.fcx
@LastEditTime: 2020-04-07 10:26:01
'''

import base64
 
with open(r"D:\Program Files\MyFile\项目文件\吕老板要的直直的星星\最终\4(已去底)(已去底).png", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    print('%s'%s)