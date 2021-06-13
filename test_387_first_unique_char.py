import unittest
import bisect

"""
write down thoughts
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # you can also use counter to freq_dict=Counter(s)
        freq_dict = {}
        for char in s:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
        for i, char in enumerate(s):
            if freq_dict[char] == 1:
                return i
        return -1


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, Solution().firstUniqChar("leetcode"))


if __name__ == '__main__':
    unittest.main()
