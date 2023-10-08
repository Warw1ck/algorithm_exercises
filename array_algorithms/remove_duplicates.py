from typing import List


def removeDuplicates(nums: List[int]) -> int:
    n = 0
    for element in set(nums):
        n += (nums.count(element) - 1)

    return n

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
