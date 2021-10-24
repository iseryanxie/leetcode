import unittest
import bisect

"""
write down thoughts
scan from left to right
cumulate the sum of chars, if num(letter)<num(letter+1), say IV, then total sum-=2*num(letter)
i.e., IV=1+5-2*1=4
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        prev = 0
        sum = 0
        for c in s:
            if c in num_map:
                sum += num_map[c]
            else:
                return 0
            if prev < num_map[c]:
                sum -= 2 * prev
            prev = num_map[c]
        return sum


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, Solution().romanToInt("III"))

    def test2(self):
        self.assertEqual(4, Solution().romanToInt("IV"))

    def test3(self):
        self.assertEqual(1994, Solution().romanToInt("MCMXCIV"))


if __name__ == '__main__':
    unittest.main()
