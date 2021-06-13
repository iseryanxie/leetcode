import unittest

"""
write down thoughts
resolve from end to start, each letter is determined by the modulo of 26.
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while columnNumber > 0:
            columnNumber -= 1  # must move one left each time to locate the right char, starting from 0
            r = columnNumber % 26
            res = alphabets[r] + res
            columnNumber = columnNumber // 26
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual('A', Solution().convertToTitle(1))
    def test2(self):
        self.assertEqual('BZ', Solution().convertToTitle(78))
    def test3(self):
        self.assertEqual('YZ', Solution().convertToTitle(676))
    def test4(self):
        self.assertEqual('ZY', Solution().convertToTitle(701))
    def test5(self):
        self.assertEqual('AZ', Solution().convertToTitle(52))


if __name__ == '__main__':
    unittest.main()
