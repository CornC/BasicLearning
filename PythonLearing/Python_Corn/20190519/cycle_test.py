'''
@Description: 循环函数练习（包括 range 类型）
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-19 12:29:16
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-20 13:31:05
'''
'''
range`以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的，例如：

`range(101)`可以产生一个0到100的整数序列。
`range(1, 100)`可以产生一个1到99的整数序列。
`range(1, 100, 2)`可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。

'''
'''
for in 循环常用于循环次数已知的情况
'''
sumx = 0
for x in range(51):
    sumx += x
print(sumx)

sumy = 0
for y in range(1, 51):
    sumy += y
print(sumy)

sumz = 0
for z in range(1, 51, 2):
    sumz += z
print(sumz)
'''
99乘法表 (嵌套循环)
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j))
    print()
'''
while 循环常用于已知终止条件但不明确循环次数的情况

即通过一个能够产生或转换出`bool`值的表达式来控制循环
'''

from random import randint

answer = randint(1, 100)
count = 0

while True:
    count += 1
    number = int(input('Please import you number :'))
    if number > answer:
        print('Smaller !')
    elif number < answer:
        print('Bigger !')
    else:
        print('Congratulation !')
        break
print('You guess count is %d' % (count))
if count > 7:
    print('You are stupid !')