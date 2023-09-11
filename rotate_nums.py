def rotate( nums, k):
    return nums[len(nums) - k:] + nums[:len(nums) - k]

print(rotate(nums = [-1,-100,3,99], k = 2))