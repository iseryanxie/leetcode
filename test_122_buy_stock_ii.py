import unittest

"""
write down thoughts
add profit for every increase step
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:  # buy and sell to get profit when the price has increased
                profit += prices[i] - prices[i - 1]
        return profit


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == '__main__':
    unittest.main()
