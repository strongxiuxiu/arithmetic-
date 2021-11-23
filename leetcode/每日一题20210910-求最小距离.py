target_set = (9, 10, 9)

s1 = [1, 23, 4, 5, 56]
s2 = [3, 100]
s3 = [-1, 8, 9]
s_list = [s1, s3, s2]
sort_List1 = sorted(s_list, key=lambda i: len(i))


def permutation_and_combination(sort_List1):
    for i in sort_List1[0]:  # 排好序的sort_List1[0]是最小的
        s_item1 = i
        for j in sort_List1[1]:
            s_item2 = j
            index = 0
            while len(sort_List1[2]) > index:
                s_item3 = sort_List1[2][index]
                index += 1
                target_set_length = abs(s_item1 - s_item2) + abs(s_item1 - s_item3) + abs(
                    s_item1 - s_item3)  # 计算长度
                print("排列组合为:{}".format((s_item1, s_item2, s_item3)), "组合长度为：{}".format(target_set_length))


permutation_and_combination(sort_List1)


def permutation_and_combination(sort_List1):
    for i, j in enumerate(sort_List1[0]):  # 排好序的sort_List1[0]是最小的
        index = 0
        left_index = 0
        s_item1 = j
        while len(sort_List1[2]) > index:
            s_item2 = sort_List1[1][left_index]
            s_item3 = sort_List1[2][index]
            index += 1
            target_set_length = abs(s_item1 - s_item2) + abs(s_item1 - s_item3) + abs(
                s_item1 - s_item3)  # 计算长度
            print("排列组合为:{}".format((s_item1, s_item2, s_item3)), "组合长度为：{}".format(target_set_length))
        left_index += 1
        # while


permutation_and_combination(sort_List1)
