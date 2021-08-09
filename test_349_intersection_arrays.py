import unittest

"""
write down thoughts
use built-in set
"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        res = []
        for num in nums2:
            if num in set1 and num not in res:
                res.append(num)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([2], Solution().intersection([1,2,2,1], [2,2]))


if __name__ == '__main__':
    unittest.main()
