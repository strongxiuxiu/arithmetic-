def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
     """
    for i in range(1, len(nums)):
        print(nums[i])
        print("max", max(nums[i - 1], 0))
        nums[i] = nums[i] + max(nums[i - 1], 0)
    print(nums)
    return max(nums)


print(maxSubArray([1, 2, -3, 4, -9, 11, -7, -10, 7, 1]))

# print(max((1, 2), (3, 4), (5, 6)))
