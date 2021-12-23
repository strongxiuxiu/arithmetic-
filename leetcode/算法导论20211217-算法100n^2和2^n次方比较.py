"""
    # 插入排序的时间时间复杂度是n^2
"""
import random
import math

from time import *


def insertion_sort(array):
    for i in range(len(array)):
        cur_index = i
        while array[cur_index - 1] > array[cur_index] and cur_index - 1 >= 0:
            array[cur_index], array[cur_index - 1] = array[cur_index - 1], array[cur_index]
            cur_index -= 1
    return array


def n_sort(n):
    while True:
        print(2**n)
        for i in range(2**n):
            pass
        break


if __name__ == '__main__':
    n = 13
    alist = [random.randint(1, 1000) for i in range(n)]
    begin_time = time()
    for i in range(100):  # 100次
        insertion_sort(alist)
    end_time = time()
    run_time = end_time - begin_time
    print("这是插入排序，时间复杂度为n^2的排序{}个元素运行的时间:{}".format(n, run_time))

    num = int(math.pow(2, n))
    begin_time = time()
    n_sort(n)
    end_time = time()
    run_time = end_time - begin_time
    print("这是插入排序，时间复杂度为n^2的排序{}个元素运行的时间:{}".format(n, run_time))