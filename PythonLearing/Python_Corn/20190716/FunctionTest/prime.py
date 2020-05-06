'''
@Description: 判断是否是素数
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-07-19 17:01:47
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-19 17:06:37
'''


def is_prime(num):
    for divisor in range(2, num // 2):
        if num % divisor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input("input Num: "))
    result = is_prime(num)
    print(result)