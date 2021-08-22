import unittest

"""
write down thoughts
BFS
each step, determine the range of indices at that step can reach.
For example, [2,3,1,1,4] 
step 0, the range is [0,0]
step 1, the range is [1,2], because at step 0, you can move 1 or 2 to the right.
step 2, the range is [3,4], the farthest you can go is 4
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0  # number of jumps
        l = r = 0  # range of the indices at the jump can reach
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1  # in next jump, start from previous r + 1
            r = farthest
            jumps += 1
        return jumps


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().jump([2, 3, 1, 1, 4]))

    def test2(self):
        self.assertEqual(2, Solution().jump([2, 3, 0, 1, 4]))


if __name__ == '__main__':
    unittest.main()
