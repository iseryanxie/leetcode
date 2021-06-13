import unittest
import bisect

"""
write down thoughts
1. Use DP
2. Define state dp[i] to denote the number of rewardable records with length i AND there is no A in such record
3. Compute dp[i]
4. Calculate the case where records does contain A using dp[i]
5. Sum the number of cases where records does or does not contain A
"""


class Solution(object):
    def checkRecord(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        M = 10**9+7
        dims = 4 if n<=3 else n+1
        dp = [0 for _ in range(dims)] # need additional space, why?
        dp[0] = 1
        dp[1] = 2 # L or P
        dp[2] = 4 # LL/LP/PL/PP
        dp[3] = 7 # PPP/PPL/PLP/LPP/PLL/LLP/LPL
        for i in range(4,n+1):
            # if new letter is P, number of awardable records for i is the same of number of awardable records for i-1
            # dp[i] = dp[i-1]
            # if new letter is L, number of awardable records for i is the number of awardable records for i-1 take out
            # the number of combinations where ....PLL, in which case another letter L will disqualify the record
            # dp[i] = dp[i-1]-dp[i-4]
            dp[i] = dp[i-1]+dp[i-1]-dp[i-4]

        # sum up the cases where there is no A
        sum = dp[n]
        for i in range(1,n+1):
            sum += (dp[i-1]*dp[n-i])%M
            # this is all the combinations of a record ...A..., where A is located at location i.
            # number of combinations for (i-1) before A multiply the number of combinations for (n-i) after A
        return sum%M



class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(8, Solution().checkRecord(2))
    def test2(self):
        self.assertEqual(183236316, Solution().checkRecord(10101))


if __name__ == '__main__':
    unittest.main()
