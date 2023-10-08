from typing import List


def firstMissingPositive(nums: List[int]) -> int:
        if 1 in nums:
            i = 2
            while True:
                if i not in nums:
                    return i
                i+=1
        else:
            return 1



print(firstMissingPositive([0]))