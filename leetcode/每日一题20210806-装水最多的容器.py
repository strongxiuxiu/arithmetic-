class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pass


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    area_list = []
    index = 0
    hg = 0
    max_c = [0, 0]
    max_area_num = 0
    # # for i in
    #     for i in range(len(height)):
    #         print(max_c,":")
    #         x = height[i]
    #         y = i + 1
    #         if max_c[0] == 0:
    #             max_c[0] = x
    #             max_c[1] = y
    #         else:
    #             print(x,33333,max_c[0])
    #             max_area = min(x, max_c[0]) * (y - max_c[1])
    #             max_c[0] = x
    #             max_c[1] = y
    #             max_area_num = max(max_area,max_area_num)
    #             print(max_area,333)

    # ['(1,1)', '(2,8)', '(3,6)', '(4,2)', '(5,5)', '(6,4)', '(7,8)', '(8,3)', '(9,7)']
    max_area = 0
    for i in range(len(height)):
        # x = i+1
        # y = height[i]
        print(i + 1, height[i], "第{}次".format(i))
        for k in range(len(height) - 1):
            # print(k)
            print(k + i, min(height[i], height[k]), "开始算后面的{}".format(k + i))
            # x = k+i
            # k+i - i+1 两个x相减
            x = k + 1
            print(height[i], height[k], 3333)
            print(min(height[i], height[k]))
            y = min(height[i], height[k] - 1)

            print(x, y, 99999999999999999999999999999999991111111)
            print(max_area, "最大值")
            if x * y > max_area:
                max_area = x * y
            # print(max_area, 2222)
    print(max_area)
    # print(k+i,3333)

    # while index < len(height):
    #     h = height[index]
    #     index += 1
    #     for i in range(len(height)):
    #         index, hg = i + 1, height[i]
    #         # print(index, hg)
    #         max_area = index * hg
    #         # print(max_area)
    #         # # print("x标为:", i + 1, 'y标为', height[i], )
    #         stare_area = "{},{}".format(i + 1, height[i])
    #         # print("{},{}".format(i + 1, height[i]))
    #         area_list.append(stare_area)
    #         print(area_list)


# max_c = [0, 0]
# height = [4, 3, 2, 1, 4]


# 输出：16
# 示例 4：
#
# height = [1, 2, 1]


# 输出：2

# def maxAreas(height):
#     """
#     :type height: List[int]
#     :rtype: int
#     """
#     max_area = 0
#     for i in range(len(height)):
#         x1 = i + 1  # 求出每个数据的X轴长度
#         y1 = height[i]  # 求出第一组数据的Y
#         for k in range(x1, len(height)):
#             x2 = k + 1
#             y2 = height[x2 - 1]
#             x = x2 - x1
#             y = min(y1, y2)
#             if x * y > max_area:
#                 max_area = x * y
#     return max_area

# height = [4, 3, 2, 1, 4]

def maxAreas(height):
    """
    # 双指针解法
    """
    left, right, max_areas = 0, len(height) - 1, 0
    while left < right:
        if height[left] < height[right]:
            min_num = min(height[left], height[right])
            max_areas = max(min_num * (right - left), max_areas)
            left += 1
        else:
            min_num = min(height[left], height[right])
            max_areas = max(min_num * (right - left), max_areas)
            right -= 1
    return max_areas


print(maxAreas(height))

# print(len(height))
