"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
通过次数554,278提交次数1,352,116
"""


# class Solution(object):
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    list_length = len(nums1) + len(nums2)
    nums3 = nums1 + nums2
    nums3.sort()
    if list_length % 2 == 0: # 偶数、
        left = list_length // 2 -1
        right = left +1
        return (nums3[left] + nums3[right])/2
    else: # 奇数
        left = list_length // 2
        return nums3[left]


if __name__ == '__main__':
    # num1 = [1, 2, 4, 5, 6,8,8,9,90]
    # num2 = [6, 7, 8, 9,78,99,1000]
    num2 = [3,4]
    num1 = [1,2]

    # print(3//2,5555)
    print(findMedianSortedArrays(num1, num2))
