import unittest

"""
write down thoughts
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """This is bruteforce or dfs recursion will timeout at test case 5, fix with a manual mem cache"""
        wordSet = set(wordDict)
        mem = {}
        def is_word(s,curr_idx):
            nonlocal mem
            if curr_idx in mem: return mem[curr_idx]
            if (curr_idx ==len(s)):
                mem[curr_idx] = True
                return True
            for word in wordDict:
                if len(word)+curr_idx<=len(s) and s[curr_idx:curr_idx+len(word)] in wordSet and is_word(s,curr_idx+len(word)):
                    mem[curr_idx] = True
                    return True
            mem[curr_idx] = False
            return False
        return is_word(s,0)

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         """DP bottom up"""
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True
#         for i in range(len(s) - 1, -1, -1):
#             for word in wordDict:
#                 if i + len(word) <= len(s) and s[i:i + len(word)] == word:
#                     dp[i] = dp[i + len(word)]
#                 if dp[i]:
#                     break
#         return dp[0]

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().wordBreak("leetcode", ["leet", "code"]))
    def test2(self):
        self.assertEqual(True, Solution().wordBreak("applepenapple", ["apple","pen"]))
    def test3(self):
        self.assertEqual(False, Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
    def test4(self):
        self.assertEqual(True, Solution().wordBreak("cars", ["car","ca","rs"]))
    def test5(self):
        self.assertEqual(False, Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
))


if __name__ == '__main__':
    unittest.main()
