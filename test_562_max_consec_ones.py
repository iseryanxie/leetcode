import unittest
import bisect

"""
write down thoughts
dynamic programming
setup an array for each position and for each direction
NOTE: need to have extra 1 row and 2 columns (why 2 extra columns, because we need the anti-diagonal element on j+2)
"""


class Solution(object):
    def longestLine(self, M) -> int:
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or len(M) == 0:
            return 0
        res = 0
        rows = len(M)
        cols = len(M[0])
        dp = [[[0 for _ in range(4)] for _ in range(cols + 2)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    # increment horizontal
                    dp[i + 1][j + 1][0] = dp[i + 1][j][0] + 1
                    res = max(res, dp[i + 1][j + 1][0])

                    # increment vertical
                    dp[i+1][j+1][1] = dp[i][j+1][1] +1
                    res = max(res, dp[i + 1][j + 1][1])

                    # increment diagonal
                    dp[i + 1][j + 1][2] = dp[i][j][2] + 1
                    res = max(res, dp[i + 1][j + 1][2])

                    # increment anti-diagonal
                    dp[i + 1][j + 1][3] = dp[i][j+2][3] + 1
                    res = max(res, dp[i + 1][j + 1][3])
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().longestLine([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]))
    def test2(self):
        self.assertEqual(0, Solution().longestLine([]))
    def test3(self):
        self.assertEqual(4, Solution().longestLine([[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]]))




if __name__ == '__main__':
    unittest.main()
