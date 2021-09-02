import unittest

"""
write down thoughts
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        streak = 0
        for num in nums:
            if num == 1:
                streak += 1
                if streak > res:
                    res = streak
            else:
                streak = 0
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))


if __name__ == '__main__':
    unittest.main()
