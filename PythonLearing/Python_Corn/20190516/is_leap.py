'''
@Description: 判断是不是闰年
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-17 15:37:30
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-17 15:41:43
'''
'''
is_leap = year % 4 == 0 & year % 100 != 0 | year % 400 == 0
'''

year = int(input('Input Year : '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap) 
