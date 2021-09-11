import unittest

"""
write down thoughts
"""
from typing import List


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg = True if num<0 else False
        if neg:
            num = -num
        res_list = []
        while num:
            res_list.append(str(num % 7))
            num = num // 7
        if neg:
            res_list.append("-")
        return "".join(reversed(res_list))


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("202", Solution().convertToBase7(100))
    def test2(self):
        self.assertEqual("0", Solution().convertToBase7(0))



if __name__ == '__main__':
    unittest.main()
