import unittest
import bisect

"""
write down thoughts
1. Use trie data structure to store the words (backwards) 
2. search in trie nodes during query, till found or not found. Since search in trie is O(N), it is efficient.
"""

from typing import List


class TreeNode:
    def __init__(self):
        self.children = {}  # use a dict to store all children
        self.is_word = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TreeNode()
        self.stream = []
        for word in words:
            self.add(word)

    def add(self,word):
        cur = self.root
        for c in word[::-1]:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.is_word = True

    def find(self):
        """find stream in trie tree nodes"""
        cur = self.root
        for i in range(len(self.stream)-1,-1,-1):
            c = self.stream[i]
            if c not in cur.children:
                return False
            cur = cur.children[c]
            if cur.is_word:
                return True
        return False

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.find()


class TestSolution(unittest.TestCase):
    def test1(self):
        streamChecker = StreamChecker(["cd", "f", "kl"]) # init
        self.assertEqual(False,streamChecker.query('a')) # return false
        self.assertEqual(False,streamChecker.query('b')) # return false
        self.assertEqual(False,streamChecker.query('c')) # return false
        self.assertEqual(True,streamChecker.query('d')) # return true, because 'cd' is in the wordlist
        self.assertEqual(False,streamChecker.query('e')) # return false
        self.assertEqual(True,streamChecker.query('f')) # return true, because 'f' is in the wordlist
        self.assertEqual(False,streamChecker.query('g')) # return false
        self.assertEqual(False,streamChecker.query('h')) # return false
        self.assertEqual(False,streamChecker.query('i')) # return false
        self.assertEqual(False,streamChecker.query('j')) # return false
        self.assertEqual(False,streamChecker.query('k')) # return false
        self.assertEqual(True,streamChecker.query('l')) # return true, because 'kl' is in the wordlist


if __name__ == '__main__':
    unittest.main()
