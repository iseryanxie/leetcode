import unittest

"""
write down thoughts
brute-force: check the each substring of the first half of the string of 
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring = ""
        for i in range(len(s) // 2):
            substring += s[i]
            if len(s) % len(substring) == 0:  # check if rep is a multiple of s
                if substring * (len(s) // len(substring)) == s:  # check if we multiply rep a few times can we get s
                    return True
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().repeatedSubstringPattern("abab"))


if __name__ == '__main__':
    unittest.main()
