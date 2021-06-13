import unittest
import bisect

"""
write down thoughts
set up a digit to char mapping, use greedy way to map
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        digit_char_map = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",
                          9: "IX", 5: "V", 4: "IV", 1: "I"}
        res = []
        while num>0:
            for k,v in digit_char_map.items():
                if num>=k:
                    res.append(v)
                    num -= k
        return "".join(res)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("III", Solution().intToRoman(3))
    def test2(self):
        self.assertEqual("LVIII", Solution().intToRoman(58))
    def test3(self):
        self.assertEqual("MCMXCIV", Solution().intToRoman(1994))


if __name__ == '__main__':
    unittest.main()
