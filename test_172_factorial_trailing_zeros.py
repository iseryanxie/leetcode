import unittest

"""
write down thoughts
determine how many 5s this number has, each 5 corresponds to 1 trailing zero, because there will be plenty of 2s.
Note: 25 contains two 5s, that corresponds to 2 zeros: 25*4=100. 
125 contains three 5s, that corresponds to 3 zeros: 125*8=1000.
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = n
        s = 0
        x = x // 5
        s += x
        while x >= 5:
            x = x // 5
            s += x
        return s


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, Solution().trailingZeroes(3))

    def test2(self):
        self.assertEqual(1, Solution().trailingZeroes(5))

    def test3(self):
        self.assertEqual(0, Solution().trailingZeroes(0))

    def test4(self):
        self.assertEqual(2, Solution().trailingZeroes(10))

    def test5(self):
        self.assertEqual(7, Solution().trailingZeroes(30))


if __name__ == '__main__':
    unittest.main()
