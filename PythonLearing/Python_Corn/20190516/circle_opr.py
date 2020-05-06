'''
@Description: 计算给定半径的圆的周长和面积
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 15:29:53
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 15:36:52
'''

'''
Perimeter = 4 * pi * radius
Area = pi * Square(radius)
'''
import math

raduis = float(input('Input Radius : '))
perimeter = 4 * math.pi * raduis
area = math.pi * math.pow(raduis,2)

print(' Perimeter is %.1f , Area is %.1f' %(perimeter,area))

