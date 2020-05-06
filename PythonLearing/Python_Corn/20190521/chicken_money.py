'''
@Description: 百鸡百钱问题
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-24 09:04:42
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-12 16:18:50
'''
'''
鸡翁一只 5钱 鸡母一只 3钱 鸡雏三只 1钱 要求100钱买100只鸡，各种几只

公鸡 x
母鸡 y
小鸡 100-x-y

5x + 3y + (100-x-y)/3 = 100

15x + 9y + 100 - x - y = 300

14x + 8y = 200
'''

for x in range(0, 100):
    for y in range(0, 100):
        if 14 * x + 8 * y - 200 == 0 and 100 - x - y >= 0:
            print("公鸡：%d 只, 母鸡：%d 只, 小鸡：%d 只" % (x, y, 100 - x - y))
