"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
通过次数281,016提交次数491,049

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random


def create_random_list(length:int, l:int, r:int):
    list1 = []
    for i in range(length):
        list1.append(random.randint(l, r))
    return list1


def min_k_num(arr, min_list, k):
    if len(min_list) == k:
        return min_list
    min_list.append(min(arr))
    arr.remove(min(arr))
    return min_k_num(arr, min_list, k)


def getleastnumbers(arr, k):
    if len(arr) == k:
        return arr
    # print(arr, "前")
    arr.remove(max(arr))
    # print(arr, "后")
    return getleastnumbers(arr, k)


def quick_sort(arr:list):
    if len(arr) < 2:
        return arr
    prv = arr[0]
    left_list = []
    right_list = []
    for i in range(1, len(arr)):
        if arr[i] > prv:
            right_list.append(arr[i])
        if arr[i] <= prv:
            left_list.append(arr[i])
    return quick_sort(left_list) + [prv] + quick_sort(right_list)


class Solution(object):
    def getLeastNumbers(self, arr:list, k:int):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]

        """
        s = Solution()
        return s.quick_sort(arr)[:k]

    def quick_sort(self, arr:list):
        if len(arr) < 2:
            return arr
        prv = arr[0]
        left_list = []
        right_list = []
        for i in range(1, len(arr)):
            if arr[i] > prv:
                right_list.append(arr[i])
            if arr[i] <= prv:
                left_list.append(arr[i])
        return quick_sort(left_list) + [prv] + quick_sort(right_list)




if __name__ == '__main__':
    random_list = create_random_list(10, 100, 200)
    print(random_list)
    print(quick_sort(random_list))
    # random_list.sort()
    # print(random_list)
    # # print(min(random_list), 999)
    # # print(min_k_num(random_list, [], 4))
    print(Solution().getLeastNumbers(random_list, 4))
    print(getleastnumbers(random_list, 4))
#