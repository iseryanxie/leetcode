import unittest

"""
write down thoughts
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:  # stick to integer operations
                return False
            n = n // 2

        return True
        # while n > 1:
        #     n /= 2 # this is less ideal, it involves float and comparison
        # return n == 1


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isPowerOfTwo(16))

    def test2(self):
        self.assertEqual(True, Solution().isPowerOfTwo(1))

    def test3(self):
        self.assertEqual(False, Solution().isPowerOfTwo(0))


if __name__ == '__main__':
    unittest.main()
