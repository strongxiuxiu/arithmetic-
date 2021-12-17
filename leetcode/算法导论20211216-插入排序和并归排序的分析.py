"""
    # 插入排序的时间时间复杂度是n^2
    # 并归排序的时间复杂度为nlg（n）
    什么情况下插入排序比并归排序快?
    前提是规定
        插入排序运行8n^2
        并归排序64nlg(n)
"""
import random

from time import *


def insertion_sort(array):
    for i in range(len(array)):
        cur_index = i
        while array[cur_index - 1] > array[cur_index] and cur_index - 1 >= 0:
            array[cur_index], array[cur_index - 1] = array[cur_index - 1], array[cur_index]
            cur_index -= 1
    return array


"""
Merge_Sort 归并排序
分治算法Divide and Conquer
时间复杂度：
"""


# 切割数组 的函数
def merge_sort(alist):
    # 如果长度小于等于1 ，不能再分割了
    if len(alist) <= 1:
        return alist

    # 根据列表长度确定拆分的中间位置
    mid_index = len(alist) // 2

    # 递归调用，无限切割下去
    left_list = merge_sort(alist[:mid_index])
    right_list = merge_sort(alist[mid_index:])
    return merge(left_list, right_list)


# 排序的函数
def merge(left_list, right_list):
    l_index, r_index = 0, 0
    merge_list = []
    # 判断列表里面是否还有元素可以用
    while l_index < len(left_list) and r_index < len(right_list):
        # 哪边的元素小于另外一边的的元素就把哪边的元素加入进去，对应的索引加一
        if left_list[l_index] < right_list[r_index]:
            merge_list.append(left_list[l_index])
            l_index += 1
        else:
            merge_list.append(right_list[r_index])
            r_index += 1
    # 下面的这两个就是，如果有一个列表全部添加了，另外一个列表直接添加到merge_list里面了
    merge_list += left_list[l_index:]
    merge_list += right_list[r_index:]
    return merge_list


if __name__ == '__main__':
    N = 2000
    alist = [random.randint(1, 1000) for i in range(N)]
    begin_time = time()
    for i in range(8):  # 这里代表8次
        insertion_sort(alist)
    end_time = time()
    run_time = end_time - begin_time
    print("这是插入排序，时间复杂度为8n^2的排序{}个元素运行的时间:{}".format(N, run_time))

    begin_time = time()
    # print('原列表的顺序{}'.format(alist))
    for i in range(64):  # 这里代表8次
        alist = merge_sort(alist)
    end_time = time()
    run_time = end_time - begin_time
    print('这是并归排序，时间复杂度为64nlg(n)的排序{}个元素所运行的时间：{}'.format(N, run_time))
