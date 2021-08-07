import unittest

"""
write down thoughts
in place swap
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1


class TestSolution(unittest.TestCase):
    def test1(self):
        s = ["h", "e", "l", "l", "o"]
        Solution().reverseString(s)
        self.assertEqual(["o", "l", "l", "e", "h"], s)


if __name__ == '__main__':
    unittest.main()
