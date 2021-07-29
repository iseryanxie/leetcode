import unittest

"""
write down thoughts
under the assumptions explained in the problem statement, we know the expected total is n*(n+1)/2, and we can calculate 
the total and then the difference is the missing number
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # there is one number missing, but it started from 0, so n=len(nums)
        expected = n * (n + 1) // 2  # 1+2+...+n = n*(n+1)/2
        actual = sum(nums)
        return expected - actual


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().missingNumber([3, 0, 1]))
    def test2(self):
        self.assertEqual(2, Solution().missingNumber([0, 1]))


if __name__ == '__main__':
    unittest.main()
