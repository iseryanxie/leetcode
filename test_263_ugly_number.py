import unittest

"""
write down thoughts
keep checking if n's prime factors include 2,3,5 or not. If n reduces to anything other than 1, it is not ugly.
pay attention to the edge case 
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n //= 2
                continue
            if n % 3 == 0:
                n //= 3
                continue
            if n % 5 == 0:
                n //= 5
                continue
            return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isUgly(6))

    def test2(self):
        self.assertEqual(False, Solution().isUgly(14))

    def test3(self):
        self.assertEqual(True, Solution().isUgly(1))

    def test4(self):
        self.assertEqual(False, Solution().isUgly(-2147483648))


if __name__ == '__main__':
    unittest.main()
