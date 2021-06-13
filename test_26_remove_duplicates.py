import unittest
import bisect

"""
write down thoughts
from 1 to n, record prev, pop duplicate, record number of removed elements
"""
from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        rm_count = 0
        for i in range(len(nums)):
            if i == 0:
                prev = nums[0]
            else:
                if nums[i-rm_count] == prev:
                    nums.pop(i-rm_count)
                    rm_count += 1
                else:
                    prev = nums[i-rm_count]
                    count += 1
        return count


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().removeDuplicates([1,1,2]))


if __name__ == '__main__':
    unittest.main()
