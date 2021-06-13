import unittest
import bisect

"""
write down thoughts
Use DP
1. for each coin set, calculate dp[j] as the number of combinations to make up amount j
with coin set [1]
dp = [1 1 1 1 1 1], because each amount has only 1 way to make of using coin 1, dp[0] is the first element
with coin set [1,2]
dp = [1 1 2 2 2 3], dp[i][j] = dp[i-1][j]+dp[i][j-coin], we are not storing each row, so it becomes dp[j]+=dp[j-coin]
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, Solution().change(5, [1, 2, 5]))
    def test2(self):
        self.assertEqual(0, Solution().change(3, [2]))


if __name__ == '__main__':
    unittest.main()
