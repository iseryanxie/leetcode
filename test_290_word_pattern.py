import unittest

"""
write down thoughts
use two hashmaps to keep track of whether the word is mapped to a pattern letter and a pattern letter is mapped to a word.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        hashmap = {}
        hashmap_inv = {}
        for i, letter in enumerate(pattern):
            if letter in hashmap and words[i] != hashmap[letter]:
                return False
            if words[i] in hashmap_inv and letter != hashmap_inv[words[i]]:
                return False
            else:
                hashmap[letter] = words[i]
                hashmap_inv[words[i]] = letter
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().wordPattern("abba", "dog cat cat dog"))

    def test2(self):
        self.assertEqual(False, Solution().wordPattern("abba", "dog cat cat fish"))

    def test3(self):
        self.assertEqual(False, Solution().wordPattern("aaaa", "dog cat cat dog"))

    def test4(self):
        self.assertEqual(False, Solution().wordPattern("abba", "dog dog dog dog"))


if __name__ == '__main__':
    unittest.main()
