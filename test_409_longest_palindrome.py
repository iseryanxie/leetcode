import unittest

"""
write down thoughts
count the occurrences of each letter, 
for letters occurred even times, length+=occurences,
if odd times, length+=occurences-1
if ever had odd times letters, length += 1 one time
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        cnt_s = Counter(s)
        res = 0
        odd_seen = 0
        for cnt in cnt_s.values():
            if cnt % 2 == 0:
                res += cnt
            else:
                res += cnt -1
                odd_seen = 1
        return res + odd_seen


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, Solution().longestPalindrome("abccccdd"))
    def test2(self):
        self.assertEqual(1, Solution().longestPalindrome("a"))
    def test3(self):
        self.assertEqual(2, Solution().longestPalindrome("dd"))


if __name__ == '__main__':
    unittest.main()
