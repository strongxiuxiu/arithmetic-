import random


# 快速排序的算法分解

def quick_sort(array: list):
    if len(array) < 2:
        # 基线条件，当数组只剩下1或者0个元素时，我们将数组return
        return array
    pivot = array[0]  # 获取一个基准值
    left_list = []
    right_list = []
    for i in range(1, len(array)):
        if array[i] > pivot:
            right_list.append(array[i])
        else:
            left_list.append(array[i])
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


def create_random_list(length: int, l: int, r: int):
    i = 0
    list1 = []
    while i < length:
        list1.append(random.randint(l, r))
        i += 1
    return list1


if __name__ == '__main__':
    random_list = create_random_list(100, 10, 200)
    print(random_list)
    print(quick_sort(random_list))
