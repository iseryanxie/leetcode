import unittest

"""
write down thoughts
Use two pointers to increment separately.
If match, both move to next until the dictionary exhausted then we know it's false. 
If not match, then the dictionary pointer move to next
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        pt = 0
        ns = len(s)
        nt = len(t)
        if nt < ns:
            return False
        while ps < ns:
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
                if pt >= nt and ps < ns:  # dictionary exhausted before the subsequence is determined
                    return False
            else:
                pt += 1
                if pt >= nt and ps < ns:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isSubsequence("abc", "ahbgdc"))

    def test2(self):
        self.assertEqual(True, Solution().isSubsequence("axc", "ahbgdc"))


if __name__ == '__main__':
    unittest.main()
