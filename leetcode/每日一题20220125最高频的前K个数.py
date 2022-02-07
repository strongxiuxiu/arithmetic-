"""
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

"""

import random


def create_random_list(length, l, r):
    new_list = []
    i = 0
    while i < length:
        new_list.append(random.randint(l, r))
        i += 1
    return new_list


def find_k_altofrequency(arr, k):

    for i in range(len(arr)):

        print(arr.count(arr[i]))
        print(i)

    pass


if __name__ == '__main__':
    random_list = create_random_list(10, 1, 5)
    print(random_list)
    find_k_altofrequency(random_list,2)
