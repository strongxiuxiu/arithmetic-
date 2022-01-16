# 理解sum函数处理办法

# 非尾递归

"""
解决问题都是：将一个列表的数组进行
"""


def total_sum(sum_list: list, num_total: int):
    if sum_list != []:
        num_total += sum_list[0]
        total_sum(sum_list[1:], num_total)
    return num_total


# 尾递归
def total_sum_tail(sum_list: list, num_total: int):
    if sum_list != []:
        num_total += sum_list[0]
        return total_sum_tail(sum_list[1:], num_total)
    return num_total


if __name__ == '__main__':
    print("非尾递归值：{}".format(total_sum([1, 2, 3, 4, 5], 0)))
    print("尾递归值:{}".format(total_sum_tail([1, 2, 3, 4, 5], 0)))
