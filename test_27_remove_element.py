import unittest
import bisect

"""
write down thoughts
1. scan from left to right, create a right pointer
2. if found val, swap values of current with right (in fact, no need to swap, just replace with the right most value), right-- 
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == val:
                nums[i] = nums[right]
                # nums[right] =0
                right -= 1  # nums[right] unknown, do not move i
            else:
                i += 1
        return i


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [3, 2, 2, 3, 5, 3, 5, 1, 3]
        val = 3
        self.assertEqual(5, Solution().removeElement(nums, val))
        # self.assertEqual([2,2,3,3],nums)

    def test2(self):
        nums = [3, 2, 2, 3]
        val = 3
        self.assertEqual(2, Solution().removeElement(nums, val))
        # self.assertEqual([2,2,3,3],nums)


if __name__ == '__main__':
    unittest.main()
