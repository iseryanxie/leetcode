import unittest

"""
write down thoughts
1. basic recursions will time out, add my own cache hashmap
2. bottom-up DP
"""


# class Solution:
#     """recursion, DP top-down"""
#     def __init__(self):
#         self.cache = {}
#
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n in self.cache:
#             return self.cache[n]
#         res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#         self.cache[n] = res
#         return res
class Solution:
    """DP bottom up"""
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = {1: 1, 2: 2}
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, Solution().climbStairs(1))

    def test2(self):
        self.assertEqual(3, Solution().climbStairs(3))


if __name__ == '__main__':
    unittest.main()
