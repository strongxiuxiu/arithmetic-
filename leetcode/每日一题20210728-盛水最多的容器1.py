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
    for i in range(len(height)):
        # print("x标为:", i+1, 'y标为', height[i], )
        stare_area = "({},{})".format(i + 1, height[i])
        # print("({},{})".format(i+1, height[i]))

        area_list.append(stare_area)
        print(area_list)


maxArea(height)
