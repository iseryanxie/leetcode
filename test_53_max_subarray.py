import unittest
import bisect

"""
write down thoughts
Kadane's algorithm
"""
from typing import List


class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_sum = max_sum = nums[0]
        for i in nums[1:]:
            dp_sum = max(dp_sum + i, i)
            # maximum sum at current position, is either maximum sum at previous postion add i or start a new series
            max_sum = max(dp_sum, max_sum)
        return max_sum


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == '__main__':
    unittest.main()
