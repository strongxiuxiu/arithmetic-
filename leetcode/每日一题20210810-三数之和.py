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
# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0]

nums = [-1, 0, 1, 0]


# nums = [0]
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    left, right = 0, len(nums) - 1
    for i in range(len(nums)):
        left = nums[i]



# list1 = []
# if len(nums)>=3:
#     nums.sort()
#     for i in range(len(nums)):
#         # nums[len(nums) - 1 - i]
#         print(i)
#         # print(nums[len(nums)-1-i])
#         aandc = 0 - nums[i]  # 拿到另外两个数的和
#         if i < len(nums) - 1:
#             # if nums[i] == 0 and nums[i + 1] not in nums[:i-1]:
#             # if nums[i + 1] not in nums[:i]:
#             left = nums[i + 1]
#             right = aandc - left
#             if right in nums[i + 1:]:
#                 if [nums[i], left, right] not in list1:
#                     list1.append([nums[i], left, right])
#             # print(left, right)
#             # i += 1
#             # else:
#
#     #     print(aandc)
#     # print(11)
#     # print(list1)
# return list1


print(threeSum(nums))

a = [[0, 0, 0]]
b = [0, 0, 0]

# b = [[1, 3, 4]]
if b in a:
    print(111)
"""
        aandc = 0 - nums[i]  # 拿到另外两个数的和
        if i < len(nums) - 1:
            # if nums[i] == 0 and nums[i + 1] not in nums[:i-1]:
            # if nums[i + 1] not in nums[:i]:
            left = nums[i + 1]
            right = aandc - left
            if right in nums[i + 1:]:
                list1.append([nums[i], left, right])
            # print(left, right)
            # i += 1
            # else:

    #     print(aandc)
    print(list1)"""
