import unittest
import bisect

"""
write down thoughts
1. left ,right two pointer
2. add left and right to ans array till left reaches n
3. space O(2n), is there a way to swap? too much trouble
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        ans = []
        if len(nums)!= 2*n:
            return ans
        while left<n and right<2*n:
            ans.append(nums[left])
            ans.append(nums[right])
            left += 1
            right += 1
        return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([2, 3, 5, 4, 1, 7], Solution().shuffle([2, 5, 1, 3, 4, 7], 3))


if __name__ == '__main__':
    unittest.main()
