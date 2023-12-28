from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m] + nums2[:n]
        nums1.sort()

s = Solution()
s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)