import unittest

"""
write down thoughts
1. use template to get each digits of the number
"""


class Solution:
    def addDigits(self, num: int) -> int:
        tmp_num = num
        tmp_sum = 0
        while tmp_num>=10:
            while tmp_num>0:
                r = tmp_num % 10
                tmp_num //= 10
                tmp_sum += r
            tmp_num = tmp_sum
            tmp_sum = 0
        return tmp_num


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().addDigits(38))


if __name__ == '__main__':
    unittest.main()
