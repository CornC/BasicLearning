'''
@Description: 函数练习 最大公倍/最小公约数
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-07-19 15:40:47
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-19 16:25:02
'''


def gys(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for divisor in range(x, 0, -1):
        if x % divisor == 0 and y % divisor == 0:
            return divisor


def gbs(x, y):
    return x * y // gys(x, y)
