"""
35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4
示例 4:

输入: nums = [1,3,5,6], target = 0
输出: 0
示例 5:

输入: nums = [1], target = 0
输出: 0


提示:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为无重复元素的升序排列数组
-104 <= target <= 104
通过次数648,662提交次数1,418,720
"""
import random


def find_insert_location(list1, target):
    left = 0
    right = len(list1) - 1
    if list1[0] > target:
        return left
    while left < right:
        num = left + right
        pub = num // 2
        if list1[pub] == target:
            return pub
        elif list1[pub] > target:
            right = pub - 1
        elif list1[pub] < target:
            left = pub + 1
    if list1[right] < target:
        return right + 1
    else:
        return right


def create_random_list(r, l, length):
    new_list = []
    for i in range(length):
        new_list.append(random.randint(r, l))
    return new_list


if __name__ == '__main__':
    new_list = set(create_random_list(1, 100, 10))
    sort_list = sorted(new_list)
    print(sort_list)
    target = 1
    sort_list = [17, 33, 40, 50, 51, 56, 72, 89, 92, 94]
    print(sort_list)
    print(find_insert_location(sort_list, target))
