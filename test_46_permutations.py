import unittest

"""
write down thoughts
Recursion:
1. deal with base cases
2. for range(len(nums)), 
    pop out the first element, 
    then recursively call permute on the rest of the list, 
    appending the first element to the end of the list. 
    Then add the whole permutation to the result.
 
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]],
                         Solution().permute([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
