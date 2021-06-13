import unittest

"""
write down thoughts
if n>=0, return x power n
else, return 1/x power n
recursive call a function to raise x*x, then n//2
"""

# class Solution:
#     def pow0(self, x, n):
#         if n == 0: return 1
#         if n == 1: return x
#         if n % 2 == 0: return self.pow0(x * x, n / 2)
#         return x * self.pow0(x * x, n // 2)
#     def myPow(self, x: float, n: int) -> float:
#
#         return self.pow0(x, n) if (n >= 0) else 1 / self.pow0(x, abs(n))
#

class Solution:
    def _power(self,x,n):
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            return self._power(x*x,n//2)
        return x*self._power(x*x,n//2)

    def myPow(self, x: float, n: int) -> float:
        return self._power(x,n) if n>=0 else self._power(1/x,-n)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(1024.0, Solution().myPow(2.0,10))
    def test2(self):
        self.assertEqual(9.261, int(Solution().myPow(2.1,3)*1000000)/1000000)
    def test3(self):
        self.assertEqual(0.25, Solution().myPow(2.0,-2))


if __name__ == '__main__':
    unittest.main()
