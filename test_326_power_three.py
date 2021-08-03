import unittest

"""
write down thoughts
all negatives are not power of 3.
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n!=1:
            if n%3 == 0:
                n //= 3
            else:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isPowerOfThree(27))
    def test2(self):
        self.assertEqual(False, Solution().isPowerOfThree(0))
    def test3(self):
        self.assertEqual(False, Solution().isPowerOfThree(45))



if __name__ == '__main__':
    unittest.main()
