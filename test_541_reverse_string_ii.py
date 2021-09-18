import unittest

"""
write down thoughts
note when you slice lst[i:i+k], i+k is out of range, it will return up to the end of the list,
it is very convenient without an index out of bound error
"""
from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)
        for i in range(0, len(lst), 2 * k):
            # lst[i:i + k] = lst[i:i + k][::-1]
            lst[i:i + k] = reversed(lst[i:i + k])
        return "".join(lst)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("bacdfeg", Solution().reverseStr("abcdefg", 2))


if __name__ == '__main__':
    unittest.main()
