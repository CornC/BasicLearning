'''
@Description: 输入三条边长如果能构成三角形就计算周长和面积
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 17:14:30
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 17:27:08
'''
'''
判断条件 ： 两边之和大于第三边
求取内容 ： 周长 = 三边之和
海伦公式 ： 面积 = sqrt(p * (p-a) * (p-b) * (p-c))  p为半周长
'''

from math import sqrt

a = int(input('Input a = '))
b = int(input('Input b = '))
c = int(input('Input c = '))

if a + b > c and a + c > b and b + c > a:
    print('Can make triangle !')
    perimeter = a + b + c
    halfp = (a + b + c) / 2
    area = sqrt(halfp * (halfp - a) * (halfp - b) * (halfp - c))

    print('Perimeter is %d' %(perimeter))
    print('Area is %.2f' %(area))
else:
    print('Can not make triangle!')

