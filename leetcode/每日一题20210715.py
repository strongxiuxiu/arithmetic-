"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000
 

提示：

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

class Solution(object):
    max_length = None

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        i = 0
        index = True
        if isinstance(self.max_length, bool) and len(nums) == 1:
            print(self.max_length, nums, 333)
            print(111)
            self.max_length = nums[0]
        while len(nums) > 0:
            if i < len(nums):
                max_num = max_num + nums[i]
                if self.max_length or isinstance(self.max_length, (int)):
                    if max_num > self.max_length:
                        self.max_length = max_num
                    i += 1
                else:
                    self.max_length = max_num
                    i += 1
            else:
                self.maxSubArray(nums[1:])
                break
        return self.max_length


print(Solution().maxSubArray(nums))

