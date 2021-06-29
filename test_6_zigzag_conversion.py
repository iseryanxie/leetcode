import unittest

"""
write down thoughts
keep numRows of separate strings, have an iterator to iterate between start and end of the numRows strings, append
characters to the end of each string, then concatenate strings together
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        tmp = ["" for i in range(numRows)]
        row = 0
        delta = -1
        for c in s:
            tmp[row]+=c
            if row == 0 or row==numRows-1:
                delta *= -1
            row += delta

        return "".join(tmp)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("PAHNAPLSIIGYIR", Solution().convert("PAYPALISHIRING",3))
    def test2(self):
        self.assertEqual("A", Solution().convert("A",1))
    def test3(self):
        self.assertEqual("A", Solution().convert("A",3))



if __name__ == '__main__':
    unittest.main()
