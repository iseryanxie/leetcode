import unittest

"""
write down thoughts
approach 1. binary search
find the largest k such that k*(k+1)<=2*n
approach 2. math formula
k = math.floor((2 * n + 0.25)**0.5 - 0.5) <= n = k*(k+1)/2
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            k = (left + right) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
#
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         return int((2 * n + 0.25)**0.5 - 0.5)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().arrangeCoins(5))


if __name__ == '__main__':
    unittest.main()
