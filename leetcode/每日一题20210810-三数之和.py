"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]


提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
通过次数596,543提交次数1,806,538
"""
nums = [-1, 0, 1, 2, -1, -4]
# nums = []
# nums = [0]
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    list1 = []
    for i in range(len(nums)):
        aandc = 0 - nums[i]  # 拿到另外两个数的和
        if i < len(nums) - 1:
            left = nums[i + 1]
            right = aandc - left
            if right in nums[i + 1:]:
                list1.append([nums[i], left, right])
            i += 1
    #     print(aandc)
    print(list1)


threeSum(nums)



a = [1,3,4]

b = [[1,3,4]]
if a in b:
    print(111)