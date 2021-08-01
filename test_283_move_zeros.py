import unittest

"""
write down thoughts
use two pointers, one to keep track of the location of the first zero, in the consecutive zeros in the end.
keep swapping the nonzeros with the first zero and leave the zeros in the end of the consecutive zeros.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # i represent the first 0 in the consecutive zeros
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]  # swap the non-zero element with the first 0 in the consective zeros
                i += 1


class TestSolution(unittest.TestCase):
    def test1(self):
        l = [0, 1, 0, 3, 12]
        Solution().moveZeroes(l)
        self.assertEqual([1, 3, 12, 0, 0], l)


if __name__ == '__main__':
    unittest.main()
