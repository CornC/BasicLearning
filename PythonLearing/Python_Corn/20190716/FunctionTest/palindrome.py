'''
@Description: 判断回文数
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-07-19 16:27:00
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-19 17:00:59
'''

def is_palindrome(num):
    temp = num
    total = 0 # total 计算的是其反序数
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

if __name__ == '__main__':
    num = int(input("input num: "))
    total = is_palindrome(num)
    print(total)