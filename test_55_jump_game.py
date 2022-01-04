import unittest

"""
write down thoughts
as long as can jump to N, any step before N is reachable, because you can choose to any step between (0, i) for each step
"""
from typing import List


class Solution:
    # Time limit exceeded
    # def canJump(self, nums: List[int]) -> bool:
    #     can_jump = {}
    #
    #     def canJump(nums: List[int], idx):
    #         if len(nums) == 1:
    #             return True
    #         if idx >= len(nums)-1:
    #             can_jump[idx] = True
    #             return True
    #         for i in range(1, nums[idx] + 1):
    #             if (idx + i) in can_jump and can_jump[idx + i]:
    #                 return True
    #             if idx + i <= len(nums) and canJump(nums, idx + i):
    #                 can_jump[idx + i] = True
    #                 return True
    #         return False
    #
    #     return canJump(nums, 0)

    # time limit exceeded
    # def canJump(self, nums: List[int]) -> bool:
    #
    #     n = len(nums)
    #     dp = [False] * (n)
    #
    #     dp[0] = True
    #
    #     for i in range(1, n):
    #         for j in range(i):
    #             if (i - j <= nums[j] and dp[j] == True):
    #                 dp[i] = True
    #                 break
    #
    #     return dp[-1]
    # Greedy, O(n)
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums) - 1

        if (len(nums) == 1):
            return True

        jump = nums[0]

        for i in range(n):
            if jump >= i:
                jump = max(jump, i + nums[i])
            if jump >= n:
                return True

        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().canJump([2, 3, 1, 1, 4]))

    def test2(self):
        self.assertEqual(True, Solution().canJump([0]))

    def test3(self):
        self.assertEqual(True, Solution().canJump([2, 0, 0]))


if __name__ == '__main__':
    unittest.main()
