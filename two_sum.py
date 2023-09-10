class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            number = nums[i]
            diff = target - number
            left_nums = nums[i + 1:len(nums)]
            if diff in left_nums:
                return [i, left_nums.index(diff) + i + 1]

solutions = Solution()
print(solutions.twoSum([-1,-2,-3,-4,-5], -8))
