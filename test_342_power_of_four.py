import unittest

"""
write down thoughts
same as power of three
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4 == 0:
                n //= 4
            else:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isPowerOfFour(16))

    def test2(self):
        self.assertEqual(False, Solution().isPowerOfFour(5))


if __name__ == '__main__':
    unittest.main()
