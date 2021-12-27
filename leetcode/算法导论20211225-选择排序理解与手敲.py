# 选择排序


def select_sort(list_1):
    for i in range(len(list_1) - 1):
        min_index = i  # 拿到最小下标
        for j in range(i + 1, len(list_1)):
            if list_1[j] < list_1[min_index]:
                min_index = j

        list_1[min_index], list_1[i] = list_1[i], list_1[min_index]


def selection_sort(list_1):
    for i in range(len(list_1) - 1):
        min_num = min(list_1[i:])
        list_1[i], list_1[list_1.index(min_num)] = list_1[list_1.index(min_num)], list_1[i]



if __name__ == '__main__':
    list1 = [55, 78678, 9, 1, 4, -3, 8, 9, 0, 444, 89, 4, 234]
    for i in list1:
        c = min(list1)
        list1[1], list1[list1.index(c)] = list1[list1.index(c)] , list1[1]
        print(list1)

    # list1[1],list1[2] = list1[2],list1[1]
    # print(list1)
    select_sort(list1)




