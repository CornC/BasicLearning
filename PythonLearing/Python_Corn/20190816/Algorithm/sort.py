'''
@Description: 部分排序、查询算法的 python 实现
@version: 
@Company: Lifegen
@Author: CornC.fcx
@Date: 2019-08-16 14:40:14
@LastEditors: CornC.fcx
@LastEditTime: 2019-08-16 16:39:14
'''

# 选择排序
def select_sort(dataList, comp = lambda x, y : x < y):
    items = dataList[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
            items[i], items[min_index] = items[min_index], items[i]
    return items

# 冒泡排序
def bubble_sort(dataList, comp = lambda x, y : x < y):
    items = dataList[:]
    for i in range(len(items) - 1):
        swap = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j+1]):
                items[j], items[j+1] = items[j+1], items[j]
                swap = True
        if swap:
            swap = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j-1], items[j]):
                    items[j-1], items[j] = items[j], items[j-1]
                    swap = True
        if not swap:
            break
    return items

# 归并排序
def merge_sort(items, comp = lambda x, y: x <= y):
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)
    
# 归并
def merge(item1, item2, comp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(item1) and index2 < len(item2):
        if comp(item1[index1], item2[index2]):
            items.append(item1[index1])
            index1 += 1
        else:
            items.append(item2[index2])
            index2 += 1
    items += item1[index1:]
    items += item2[index2:]
    return items

# 顺序查找
def seq_search(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

# 折半查找
def bin_search(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1
