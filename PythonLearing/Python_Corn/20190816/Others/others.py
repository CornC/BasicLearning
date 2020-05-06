'''
@Description: 一些常用的和推荐使用的语法 以及 一些工具的使用
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-19 10:11:53
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-19 10:47:18
'''

# 使用生成式语法生成列表、集合和字典

# 字典
prices = {
    'A' : 190,
    'B' : 180,
    'C' : 110,
    'D' : 50,
    'E' : 70,
    'F' : 120
}
# 价格大于 100 的构成新字典
prices2 = {key : value for key, value in prices.items() if value > 100}
print(prices2)

# 列表
numset = [i for i in range(60) if i % 3 == 0]
print(numset)

# 嵌套列表
names = [['A', 'B', 'C', 'D'], ['AA', 'ACC', 'DB']]
myset = [name for lst in names for name in lst if name.count('A') == 2]
print(myset)

# 集合 (自带去重功能)
squared = {x**2 for x in [1, -1, 2]}
print(squared)

# heapq、itertools等的用法

import heapq
# 创建堆的两种方式
# 1
# heapq.heappush(heap, item)
# 将一个 item 加入堆中， 保持堆的结构


