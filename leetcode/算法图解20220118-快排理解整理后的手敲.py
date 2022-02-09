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


# 年假后的快速排序试敲
def quick_sort_(list1):
    if len(list1) < 2:
        return list1
    pov = list1[0]
    left_list = []
    right_list = []
    for i in range(1, len(list1)):
        if list1[i] > pov:
            right_list.append(list1[i])
        else:
            left_list.append(list1[i])
    return quick_sort_(left_list) + [pov] + quick_sort_(right_list)


if __name__ == '__main__':
    random_list = create_random_list(100, 10, 200)

    print(random_list)
    print(quick_sort(random_list))
