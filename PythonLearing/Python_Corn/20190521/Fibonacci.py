'''
@Description: 实现斐波那契数列
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-07-12 16:19:41
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-12 16:51:45
'''
'''
表达式 F[n]=F[n-1]+F[n-2](n>=3,F[1]=1,F[2]=1)
'''

'''
1
'''
def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

# fib(100)

'''
2
'''
i = 1
j = 1
print(i)
print(j)
for x in range(2, 100):
    if x == i + j:
        print(x)
        j = i
        i = x
