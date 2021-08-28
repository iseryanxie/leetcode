import unittest

"""
write down thoughts
increment n-1 elements is equivalent to decrement one of the element,
therefore, the question is equivalent to decrement one element by 1 until
all of the elements equals to the minimum of the elements
"""

from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        res = 0
        for num in nums:
            res += num-min_num
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().minMoves([1,2,3]))


if __name__ == '__main__':
    unittest.main()
