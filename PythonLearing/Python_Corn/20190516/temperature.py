'''
@Description: 华氏温度转换成摄氏度
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 15:23:02
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 15:29:13
'''

'''
F = 1.8C + 32
'''

f = float(input('F = '))
c = (f - 32) / 1.8
print('%.1f F = %.1f C' %(f,c))