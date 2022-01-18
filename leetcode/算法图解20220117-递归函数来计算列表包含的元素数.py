import random


# 找出列表中的最大值 # 计算列表包含的元素数

def count_list_size(list1: list, sum_num: int, max_num: int):
    if len(list1) < 1:
        return sum_num, max_num
    if max_num:
        if list1[0] > max_num:
            max_num = list1[0]
    else:
        max_num = list1[0]
    sum_num += list1[0]
    return count_list_size(list1[1:], sum_num, max_num)


def create_random_list(length: int, head: int, trail: int):
    list_random = []
    i = 0
    while i < length:
        list_random.append(random.randint(head, trail))
        i += 1
    return list_random


if __name__ == '__main__':
    list1 = create_random_list(20, 0, 100)
    print(list1)
    print(count_list_size(list1, sum_num=0, max_num=False))
