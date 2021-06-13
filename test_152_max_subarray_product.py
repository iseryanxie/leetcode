import unittest
import bisect

"""
write down thoughts
variation of Kardane's algorithm, to record both the most positive and most negative, because the sign can flip
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_prod, min_prod = nums[0], nums[0]
        res = max_prod # start res with one number in nums to handle when there is only 1 nums and it is negative
        for num in nums[1:]:
            tmp = max(num, num * max_prod, num * min_prod)
            min_prod = min(num, num * max_prod, num * min_prod)
            max_prod = tmp
            res = max(max_prod, res)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, Solution().maxProduct([2, 3, -2, 4]))
    def test2(self):
        self.assertEqual(48, Solution().maxProduct([2, 3, -2, 4,-1]))
    def test3(self):
        self.assertEqual(0, Solution().maxProduct([-2,0,-1]))


if __name__ == '__main__':
    unittest.main()
