'''
@Description: 判断一个数是不是素数
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-20 13:32:16
@LastEditors: CornC.fcx
@LastEditTime: 2019-05-20 13:41:48
'''

'''
素数的判断条件：
除了1和本身 不能被其他数整除
'''

from math import sqrt

num = int(input('Input a number :'))
end = int(sqrt(num))
is_prime = True

for i in range(2,end+1):
    if num % i == 0:
        is_prime = False
        break
        
if is_prime == True and num != 1:
    print('%d is Prime Number' %(num))
else:
    print('%d is Not Prime Number' %(num))
