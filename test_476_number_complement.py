import unittest

"""
write down thoughts
find the next highest power of 2 greater than num: n
the result is just the n xor the num
"""


class Solution:
    def findComplement(self, num: int) -> int:
        n = 1
        while n <= num:
            n *= 2
        return num ^ (n - 1)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().findComplement(5))


if __name__ == '__main__':
    unittest.main()
