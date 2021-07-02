import unittest

"""
write down thoughts
read char from string, each shift in char represents 26 repetitions
use ord() to calculate the shifts
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res = res*26+ord(c)-ord('A')+1
        return res


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     self.assertEqual(1, Solution().titleToNumber("A"))
    def test2(self):
        self.assertEqual(28, Solution().titleToNumber("AB"))
    def test3(self):
        self.assertEqual(701, Solution().titleToNumber("ZY"))
    def test4(self):
        self.assertEqual(2147483647, Solution().titleToNumber("FXSHRXW"))



if __name__ == '__main__':
    unittest.main()
