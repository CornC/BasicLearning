'''
@Description: 完全数（完美数）
@version: 1.0
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-24 08:42:13
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-12 16:10:55
'''

'''
完全数是  该数恰好等于其因子之和
'''

for i in range(2, 101):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print("Perfect Num : %d" % i)
