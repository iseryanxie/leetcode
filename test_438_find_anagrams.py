import unittest

"""
write down thoughts
store a key-value map (key is the char and value is how many times it has in the window)
for a sliding window of substring and compare it with p, update the map when slide to right
"""
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str):
        lp = len(p)
        ls = len(s)
        res = []
        if lp == 0 or lp > ls:
            return res
        p_dict = defaultdict(int)
        for c in p:
            if c not in p_dict:
                p_dict[c] = 1
            else:
                p_dict[c] += 1
        s_dict = defaultdict(int)
        for i in range(lp):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        for i in range(ls - lp + 1):
            if s_dict == p_dict:
                res.append(i)
            if i + lp < ls:
                if s_dict[s[i]] > 1:
                    s_dict[s[i]] -= 1
                else:
                    s_dict.pop(s[i]) # remove from dict if 1, or not found
                s_dict[s[i + lp]] += 1
            else: # no need to update s_dict, it's the end of the s string
                break

        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([0, 6], Solution().findAnagrams("cbaebabacd", "abc"))

    def test2(self):
        self.assertEqual([], Solution().findAnagrams("abc", "cbaebabacd"))

    def test3(self):
        self.assertEqual([0,1,2], Solution().findAnagrams("abab", "ab"))


if __name__ == '__main__':
    unittest.main()
