import unittest
import bisect

"""
write down thoughts
Do not merge and sort, time complexity is O((m+n)*log(m+n))
Do not merge sort, time complexity is O(m+n), space is O(m+n)
1. use three pointer, starting from largest to smallest
2. put the larger number to the end, move to left
3. handle the case when nums2 finishes later
space: O(1)
time: O(m+n)
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        # no need to handle remaining nums1, they are sorted and remains on the left of the array
        while j>=0: # handle remaining nums2, if any
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class TestSolution(unittest.TestCase):
    def test1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual([1, 2, 2, 3, 5, 6], nums1)


if __name__ == '__main__':
    unittest.main()
