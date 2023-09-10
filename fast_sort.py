from typing import List


def quick_sort(nums1: List[int], nums2: List[int]) -> list[int]:

    nums1 = nums1 + nums2
    for i in range(len(nums1)):
        swapped = False
        for j in range(0, len(nums1)-1-i):
            if nums1[j] > nums1[j+1]:
                nums1[j+1], nums1[j], = nums1[j], nums1[j+1]
                swapped = True
        if not swapped:
            break

    return nums1

