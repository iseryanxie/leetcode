import unittest

"""
write down thoughts
use hashmap to store not matched number
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = {}
        for num in nums:
            if num not in single:
                single[num] = 1
            else:
                del single[num]
        for i in single:
            return i


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().singleNumber([2, 2, 1]))

    def test2(self):
        self.assertEqual(4, Solution().singleNumber([4, 1, 2, 1, 2]))


if __name__ == '__main__':
    unittest.main()
