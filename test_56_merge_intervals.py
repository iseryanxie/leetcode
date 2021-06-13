import unittest
import bisect

"""
write down thoughts
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals first
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i][1], intervals[i - 1][1])
                intervals.pop(i)
            else:
                i += 1

        return intervals


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[1, 6], [8, 10], [15, 18]], Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))


if __name__ == '__main__':
    unittest.main()
