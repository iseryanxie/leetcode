import unittest

"""
write down thoughts
1. DP
Save two states.
1. Min Price as of Day i, min_price(i)
2. Max Profit as of Day i, max_profit(i)
State transition equation:
min_price(i) = min(min_price(i-1),price(i))
max_profit(i) = max(max_profit(i-1),price(i)-min_price(i))

Tips: no need to save as arrays, because it only depends on previous state.
Space Complexity: O(1)
Time Complexity: O(n)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            # update min_price first
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, Solution().maxProfit([7, 1, 5, 3, 6, 4]))

    def test2(self):
        self.assertEqual(0, Solution().maxProfit([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    unittest.main()
