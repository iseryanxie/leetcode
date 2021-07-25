import unittest

"""
write down thoughts
time complexity: O(n)
space complexity: O(1), a constant to the number of different characters in characters set.
use only one hashmap to keep the differences in appearances of characters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
            if t[i] not in hashmap:
                hashmap[t[i]] = -1
            else:
                hashmap[t[i]] -= 1
        for item in hashmap.values():
            if item != 0:
                return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isAnagram("anagram", "nagaram"))

    def test2(self):
        self.assertEqual(False, Solution().isAnagram("rat", "car"))


if __name__ == '__main__':
    unittest.main()
