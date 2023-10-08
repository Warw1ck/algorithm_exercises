from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
        return min([nums.pop(nums.index(max(nums))) for i in range(k)])






