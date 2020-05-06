'''
@Description: 测试列表的生成语法的不同方式 以及 常用数据结构 (集合、字典)
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-07-31 17:07:40
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-01 15:44:29
'''

import sys


def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x**2 for x in range(1, 10)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)

    f = list(x**2 for x in range(1, 10))
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x**2 for x in range(1, 10))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def testYield():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    # main()

    set1 = {1, 2, 3, 3, 3, 2}
    set2 = set(range(1, 5))
    set3 = set((1, 2, 3, 4, 5))  # 元组转化为集合

    set2.discard(5)

    #     print(set1)
    #     print(set2)

    # 集合的交集 并集 差集 对称差

    #     print(set1 & set2)
    #     print(set1.intersection(set2))
    #     print(set1 | set2)
    #     print(set1.union(set2))
    #     print(set1 - set2)
    #     print(set1.difference(set2))
    #     print(set1 ^ set2)
    #     print(set1.symmetric_difference(set2))

    # 子集 超集

    #     print(set1 >= set2)
    #     print(set1.issuperset(set2))
    #     print(set1 <= set2)
    #     print(set1.issubset(set2))

    # print(set3.pop())
    # testYield()

    dic = {'a': 1, 'b': 2, 'c': 3}

    print(dic['a'])

    # 对字典的遍历实际上是对键的遍历

    # 修改字典的元素

    dic['a'] = 4

    print(dic)
    
    dic.update(b = 5)
    
    print(dic)

    print(dic.get('a'))
    print(dic.get('a', 6))
    print(dic.popitem())
    print(dic.pop('c', 6))
    print(dic)