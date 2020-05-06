'''
@Description: 水仙花数(阿姆斯特朗数)
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-05-21 13:51:58
@LastEditors: CornC.fcx
@LastEditTime: 2019-07-12 16:10:00
'''
'''
水仙花数 其每个位上的数字的 3 次幂之和是它本身  如： 153 = 1^3 + 5^3 + 3^3

水仙花数严格来说是三位数
'''


def narcissictic_num(num):
    length = len(str(num))
    count = length
    num_sum = 0

    while count:
        num_sum += ((num // 10**(count - 1)) % 10)**length
        count -= 1
    else:
        if num_sum == num:
            print(' %d is Narcissistic Number !' % num)
        else:
            print(' %d is Not Narcissistic Number !' % num)


def narcissictic_num_all(num):
    original_num = num
    num_str = str(original_num)
    length = len(num_str)
    count = length
    num_sum = 0

    while count:
        num_sum += int(num_str[count - 1])**length
        count -= 1


num = int(input('Please Input A Three Bit Number : '))

narcissictic_num(num)
