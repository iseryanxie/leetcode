import unittest

"""
write down thoughts
- use shift operation
- any integer can be written as for example 10 = 3*(2**1)+3*(2**0) = 3*(2**1+2**0)
- use max of 31 shifts. 
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        if dividend == 0:
            return 0
        is_neg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        shift = 31
        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            while (dividend < divisor << shift):
                shift -= 1
            dividend -= divisor << shift
            res += 1 << shift
        return -res if is_neg else res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().divide(10, 3))

    def test2(self):
        self.assertEqual(-2, Solution().divide(7, -3))

    def test3(self):
        self.assertEqual(0, Solution().divide(0, 1))

    def test4(self):
        self.assertEqual(1, Solution().divide(1, 1))


if __name__ == '__main__':
    unittest.main()
