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


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.is_word = True

    def find(self, word: str, node: TreeNode) -> bool:
        cur = node
        if len(word) == 0:
            if cur.is_word:
                return True
            else:
                return False
        c = word[0]
        if c != "." and c not in cur.children:
            return False
        elif c in cur.children:
            return self.find(word[1:], cur.children[c])
        else:
            for nodec, node in cur.children.items():
                if self.find(word[1:], node):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self.find(word, self.root)


["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search", "search",
 "search", "search", "search", "search"]
[[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]]


class TestSolution(unittest.TestCase):
    # def test1(self):
    #     wordDictionary = WordDictionary()
    #     wordDictionary.addWord("bad")
    #     wordDictionary.addWord("dad")
    #     wordDictionary.addWord("mad")
    #     self.assertEqual(False,wordDictionary.search("pad"))  # return False
    #     self.assertEqual(True,wordDictionary.search("bad"))  # return True
    #     self.assertEqual(True,wordDictionary.search(".ad"))  # return True
    #     self.assertEqual(True,wordDictionary.search("b.."))  # return True
    def test2(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("at")
        wordDictionary.addWord("and")
        wordDictionary.addWord("an")
        wordDictionary.addWord("add")
        self.assertEqual(False, wordDictionary.search("a"))
        self.assertEqual(False, wordDictionary.search(".at"))
        wordDictionary.addWord("bat")
        self.assertEqual(True, wordDictionary.search(".at"))


if __name__ == '__main__':
    unittest.main()
