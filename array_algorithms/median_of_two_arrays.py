from typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    numbers = sorted(nums1 + nums2)
    counts = len(numbers)
    if counts % 2 == 0:
        return (numbers[counts // 2 - 1] + numbers[counts // 2]) / 2
    else:
        return numbers[counts // 2]