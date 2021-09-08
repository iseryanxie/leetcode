import unittest

"""
write down thoughts
find corresponding row, if any letter not match row number, then break the loop and use for..else to catch the break 
cases.
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key_map = {}
        for key in "qwertyuiopQWERTYUIOP":
            key_map[key] = 0
        for key in "asdfghjklASDFGHJKL":
            key_map[key] = 1
        for key in "zxcvbnmZXCVBNM":
            key_map[key] = 2
        res = []
        for word in words:
            row = key_map[word[0]]
            for letter in word:
                if key_map[letter] != row:
                    break
            else:
                res.append(word)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["Alaska", "Dad"], Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))


if __name__ == '__main__':
    unittest.main()
