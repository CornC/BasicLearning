'''
@Description: 求两个数的最大公约数和最小公倍数
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-20 13:44:08
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-20 14:17:06
'''

'''
输入两个数：
    最大公约数 即能够整除这两个数的最大值
    最小公倍数 即能够被这两个数整除的最小值
'''

num1 = int(input('Input Num 1 : '))
num2 = int(input('Input Num 2 : '))

if num1 > num2:
    num1, num2 = num2, num1

for factor in range(num1,0,-1):
    if num1 % factor == 0 and num2 % factor == 0:
        print('最大公约数是： %d' % factor)
        print('最小公倍数是： %d' % (num1 * num2 // factor))
        break

