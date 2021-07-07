import unittest

"""
write down thoughts
Use << and >> to shift digit. 
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for _ in range(32):
            counter += n & 1
            n = n >> 1
        return counter


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().hammingWeight(3))

    def test2(self):
        self.assertEqual(2, Solution().hammingWeight(3))


if __name__ == '__main__':
    unittest.main()
