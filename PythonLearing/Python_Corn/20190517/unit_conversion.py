'''
@Description: 英制单位与公制单位互换
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 16:48:22
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 16:59:02
'''

'''
1英寸=25.4毫米，1英尺=12英寸，1英寸=8英分。
'''

value = float(input('Input Value : '))
unit = input('Input Unit : ')
if unit == 'in' or unit == '英寸':
    print('%f 英寸 = %f 毫米' %(value, value * 25.4 ))
elif unit == 'mm' or unit == '毫米':
    print('%f 毫米 = %f 英寸' %(value, value / 25.4))
else:
    print('单位无效')

    
