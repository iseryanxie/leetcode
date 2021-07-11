import unittest

"""
write down thoughts
use two hashmaps to track the mapping to make sure the char is mapped and only mapped to one char
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap1 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmap and t[i] not in hashmap1:
                hashmap[s[i]] = t[i]
                hashmap1[t[i]] = s[i]
            else:
                if hashmap.get(s[i]) != t[i]:
                    return False
                if hashmap1.get(t[i]) != s[i]:
                    return False
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isIsomorphic("egg","add"))
    def test2(self):
        self.assertEqual(False, Solution().isIsomorphic("foo","bar"))
    def test3(self):
        self.assertEqual(False, Solution().isIsomorphic("badc","baba"))



if __name__ == '__main__':
    unittest.main()
