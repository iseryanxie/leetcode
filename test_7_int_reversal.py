import unittest
import bisect

"""
write down thoughts
1. check negative or not
2. template to get digit from right to left
3. accumulate digits till remaining is 0 (check if ans is too large)
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = True
            x = -x
        else:
            neg = False
        ans = 0
        while x > 0:
            cur = x % 10
            ans = ans * 10 + cur
            x = x // 10
        if ans > 2 ** 31-1:
            ans = 0
        return -ans if neg else ans


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(-321, Solution().reverse(-123))


if __name__ == '__main__':
    unittest.main()
