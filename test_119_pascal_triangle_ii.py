import unittest

"""
write down thoughts
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        for i in range(1, rowIndex):
            tmp = [1]
            for c in range(1, len(row)):
                tmp.append(row[c - 1] + row[c])
            tmp.append(1)
            row = tmp
        return row


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([1, 3, 3, 1], Solution().getRow(3))

    def test2(self):
        self.assertEqual([1, 1], Solution().getRow(1))

    def test4(self):
        self.assertEqual([1, 4, 6, 4, 1], Solution().getRow(4))


if __name__ == '__main__':
    unittest.main()
