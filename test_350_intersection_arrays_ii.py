import unittest

"""
write down thoughts
use Counter to find number of occurences, intersect is the min of the number of occurences.
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        res = []
        for item in dict1:
            if item in dict2:
                for i in range(min(dict1[item],dict2[item])):
                    res.append(item)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,2], Solution().intersect([1,2,2,1], [2,2]))


if __name__ == '__main__':
    unittest.main()
