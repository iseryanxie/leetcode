import unittest

"""
write down thoughts
start from right to left, add 1 to the first digit from the right, propagate carry to the left
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        for i, d in enumerate(digits[::-1]):
            if i == 0:
                if d + carry + 1 > 10:
                    d = 1
                    carry = 1
                elif d + carry + 1 > 9:
                    d = 0
                    carry = 1
                else:
                    d += 1
                    carry = 0
            else:
                if d + carry > 9:
                    d = 0
                    carry = 1
                else:
                    d = d + carry
                    carry = 0
            res.append(d)
        if carry == 1:
            res.append(1)

        return res[::-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([1, 2, 4], Solution().plusOne([1, 2, 3]))

    def test2(self):
        self.assertEqual([9, 0, 0], Solution().plusOne([8, 9, 9]))


if __name__ == '__main__':
    unittest.main()
