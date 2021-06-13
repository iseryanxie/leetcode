import unittest
import bisect

"""
write down thoughts
scan digits from left to right, append combinations of letters to each of the items in the current list
each time pop the first from left of the current list, then append new ones toward the end
example "23": ["a","b","c"]->["b","c","ad","ae","af"]->["c","ad","ae","af","bd","be","bf"]...
return the current list when digits are exhausted
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        :type nums: List[int]
        :rtype: int
        """
        digit_map = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                     "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        res = [""]
        if len(digits) == 0:
            return []
        for d in digits:
            for i in range(len(res)): # pop out len(res) time for last round
                combo = res.pop(0) # pop the first one
                for tail in digit_map[d]: # assume d is always 2-9
                    res.append(combo+tail)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], Solution().letterCombinations("23"))
    def test2(self):
        self.assertEqual([], Solution().letterCombinations(""))
    def test3(self):
        self.assertEqual(["a","b","c"], Solution().letterCombinations("2"))



if __name__ == '__main__':
    unittest.main()
