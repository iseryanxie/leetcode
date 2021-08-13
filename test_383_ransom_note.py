import unittest

"""
write down thoughts
Use a counter to store the char count from magazine. When the char in ransomNote is not in magazine or running
out of counts, return False
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cnt = Counter(magazine)
        for i in ransomNote:
            if i in cnt and cnt[i] >= 1:
                cnt[i] -= 1
            else:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().canConstruct("aa", "aab"))

    def test2(self):
        self.assertEqual(False, Solution().canConstruct("aa", "ab"))


if __name__ == '__main__':
    unittest.main()
