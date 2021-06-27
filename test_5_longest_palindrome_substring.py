import unittest

"""
write down thoughts
for each point in the string, try to expand from the point (or the adjacent points) to get longest string,
return the longest found after each point is enumerated.
NOTE: be careful with the boundaries
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def longest_par_start(l, r):
            """returns the start and end(not inclusive) position of parlindrome string when s[l:r] is already a parlindrome"""
            while l >= 0 and r < n and s[l] == s[r]: # not DP but uses DP idea
                l -= 1
                r += 1
            return l + 1, r

        longest = 0
        start, end = 0, 0
        for i in range(n):
            l1, r1 = longest_par_start(i, i)
            l2, r2 = longest_par_start(i, i + 1)
            if r1 - l1 <= r2 - l2:
                par_len = r2 - l2
                tmp_start = l2
                tmp_end = r2
            else:
                par_len = r1 - l1
                tmp_start = l1
                tmp_end = r1
            if par_len <= longest:
                continue
            longest = par_len
            start = tmp_start
            end = tmp_end
        return s[start:end]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, len(Solution().longestPalindrome("cbbd")))
    def test2(self):
        self.assertEqual(3, len(Solution().longestPalindrome("babad")))
    def test3(self):
        self.assertEqual(1, len(Solution().longestPalindrome("ac")))



if __name__ == '__main__':
    unittest.main()
