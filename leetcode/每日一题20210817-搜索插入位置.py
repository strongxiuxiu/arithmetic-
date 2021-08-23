""""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4
示例 4:

输入: nums = [1,3,5,6], target = 0
输出: 0
示例 5:

输入: nums = [1], target = 0
输出: 0
 

提示:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为无重复元素的升序排列数组
-104 <= target <= 104
通过次数462,768提交次数990,803

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

nums = [1, 3, 5, 6]
target = 2

# def searchInsert1(nums, target):
#     for index, i in enumerate(nums):
#         print(index,i)
#         print(nums[index],target,444)
#         if nums[index] == target:
#             return index
#         elif nums[index] < target < nums[index + 1]:
#             return index + 1
#         elif nums[index] > target:
#             return 0
#         elif nums[index] < target:
#             return len(nums)
#         # else:
#         #     continue

#
nums1 = [1, 3, 5, 6]
nums = [1, 3, 5, 6]
target = 0


def searchInsert1(nums, target):
    # print(len(nums))
    if len(nums) > 1:
        tar = len(nums) // 2
        median = nums[tar]
        if target < median:
            searchInsert1(nums[:tar - 1], target)  # 取左边的
        elif target > median:
            searchInsert1(nums[tar + 1:], target)  # 取右边的
        else:
            return nums1.index(median)
    else:
        if nums[0] < target:
            # print(nums1.index(nums[0]) + 1,3333)
            return nums1.index(nums[0]) + 1
        else:
            return 0
    # else:
    #     if nums[0] < target:
    #         return nums1.index(nums[0]) + 1
    #     else:
    #         return 0
    # elif len(nums)<=1:
    #     if target>nums[0]:
    #         return 1
    #     else:
    #         return 0
    # else:
    #     if target > nums[0] and target < nums[1]:
    #         return nums1.index(nums[0])
    #     elif target > nums[0]:
    #         return nums1.index(nums[0]) + 1
    #     elif target < nums[1]:
    #         return nums1.index(nums[1]) + 1


print(searchInsert1(nums, target))
5
print(1111)

page = 0
page = (100+10-1)// 10
# if page == 0:
#     page = 1
print(page)
