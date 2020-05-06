'''
@Description: 掷骰子决定干什么
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 17:00:38
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 17:04:47
'''

from random import randint

diac = randint(1, 6)

if diac == 1:
    print('1')
elif diac == 2:
    print('2')
elif diac == 3:
    print('3')
elif diac == 4:
    print('4')
elif diac == 5:
    print('5')
else:
    print('6')

