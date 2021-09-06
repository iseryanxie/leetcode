import unittest

"""
write down thoughts
use hashmap to store the count of each occurence. Then run the backtrack on the hashmap to make sure there is no 
duplicates in the permutation.
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        count = Counter(nums)
        res = []
        perm = []

        def dfs():
            if len(nums) == len(perm):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    perm.append(n)
                    dfs()
                    count[n] += 1
                    perm.pop()

        dfs()
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[1, 1, 2],
                          [1, 2, 1],
                          [2, 1, 1]], Solution().permuteUnique([1, 1, 2]))


if __name__ == '__main__':
    unittest.main()
