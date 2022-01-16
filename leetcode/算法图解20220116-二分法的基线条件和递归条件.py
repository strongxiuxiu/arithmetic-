import random


# 生成一个有序列表
def binary_find(list1, num1):
    n = len(list1)
    if n < 1:
        return None
    middle_index = n // 2  # 获取中间的下标
    if num1 == list1[middle_index]:  # 如果num1==middle_index直接输出结果
        return True
    elif num1 < list1[middle_index]:  # 如果num1 小于middle_index则取middle_index之前的下标再进行查询
        return binary_find(list1[0:middle_index], num1)
    elif num1 > list1[middle_index]:  # 如果num1 大于middle_index则取middle_index之后的下标再进行查询
        return binary_find(list1[middle_index + 1:], num1)


if __name__ == '__main__':
    sort_list = list(range(1, 50, 2))  # 获取一个有序列表
    random_num1 = random.randint(1, 50)
    # print(binary_find(sort_list, num1=random_num1))
    # print("我想在{}里找到{}".format(sort_list, random_num1))
    print(binary_find([1], num1=1))
    print("我想在{}里找到{}".format([1], 1))
