import unittest

"""
write down thoughts
- ord(c)-ord('0') converts char to integer
- create a sign as a flag to track if the number has started
- calculate the number backward before it is out of bound of the integer
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        num = 0
        for c in s:
            if c == " " and not sign:  # 1 or -1 are truthy, 0 is falsy
                continue
            if c == "+" and not sign:
                sign = 1
                continue
            if c == "-" and not sign:
                sign = -1
                continue
            if not c.isdigit():
                if not sign:
                    return 0
                else:
                    break
            digit = ord(c) - ord('0')
            if sign == 1 and (2 ** 31 - 1 - digit) / 10 < num:
                return 2 ** 31 - 1
            if sign == -1 and (2 ** 31 - digit) / 10 < num:
                return -2 ** 31
            num = 10 * num + digit
            if not sign:
                sign = 1
        return sign * num


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(42, Solution().myAtoi("42"))

    def test2(self):
        self.assertEqual(-2147483648, Solution().myAtoi("-91283472332"))

    def test3(self):
        self.assertEqual(0, Solution().myAtoi("words and 987"))

    def test4(self):
        self.assertEqual(4193, Solution().myAtoi("4193 with words"))

    def test5(self):
        self.assertEqual(-42, Solution().myAtoi("   -42"))

    def test6(self):
        self.assertEqual(3, Solution().myAtoi("3.14159"))

    def test7(self):
        self.assertEqual(0, Solution().myAtoi("+-12"))


if __name__ == '__main__':
    unittest.main()
