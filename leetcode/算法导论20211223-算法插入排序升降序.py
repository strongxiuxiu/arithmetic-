"""
    插入排序
    原理：打扑克，从第二张牌开始依次和前面的牌进行比大小方放位置
"""


# 插入排序倒序
def insertion_sort(a_list):
    if len(a_list) >= 2:
        for j in range(1, len(a_list) + 1):
            # j 等于下标的从元素列表第二个开始取值
            while j < len(a_list) and j - 1 >= 0:
                if a_list[j - 1] > a_list[j]:  # > 升序  < 降序
                    a_list[j], a_list[j - 1] = a_list[j - 1], a_list[j]
                    j = j - 1
                else:
                    break
    return a_list


if __name__ == '__main__':
    list1 = [55, 78678, 9, 1, 4, -3, 8, 9, 0, 444, 89, 4, 234]
    print(insertion_sort(list1))
