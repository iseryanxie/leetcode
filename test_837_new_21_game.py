import unittest
import bisect

"""
write down thoughts
DP
1. define dp[i] to be the probablity of winning when start with point i. dp[0] is the final answer
2. dp[i] = 1/W*(dp[i+1]+dp[i+2]+...+dp[i+W])
"""


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # initialize dp
        dp = [0 for _ in range(K+W)]
        for k in range(K,min(N+1,K+W)):
            dp[k] = 1.0

        # Use sliding window to speed up sum
        sum_window = min(N-K+1,W) # initial value of sum for sliding window
        # if W is big, add prob up to N-K+1; if W is small, only add prob up to K+W
        for k in range(K-1,-1,-1):
            dp[k] = sum_window/float(W)
            sum_window += dp[k]-dp[k+W]

        return round(dp[0],5)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1.0, Solution().new21Game(10,1,10))
    def test2(self):
        self.assertEqual(0.73278, Solution().new21Game(21,17,10))



if __name__ == '__main__':
    unittest.main()
