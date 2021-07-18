import unittest

"""
write down thoughts
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        if len(nums) == 1:
            return [str(num) for num in nums]
        for i, num in enumerate(nums):
            if i == 0:
                prev = num
                start = num
                continue
            if num != prev + 1: # next consecutive number
                if start == prev: # same number
                    range = str(start)
                else: # a range
                    range = str(start) + "->" + str(prev)
                start = num
                res.append(range)
            prev = num
            if i == len(nums) - 1: # last number if range is still extending, close the range
                if start == prev:
                    range = str(start)
                else:
                    range = str(start) + "->" + str(prev)
                res.append(range)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["0->2", "4->5", "7"], Solution().summaryRanges([0, 1, 2, 4, 5, 7]))

    def test2(self):
        self.assertEqual(["0"], Solution().summaryRanges([0]))

    def test3(self):
        self.assertEqual([], Solution().summaryRanges([]))


if __name__ == '__main__':
    unittest.main()
