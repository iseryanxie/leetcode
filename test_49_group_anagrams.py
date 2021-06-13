import unittest

"""
write down thoughts
setup a hashmap to store (sorted chars)->List of strings
"""

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return [[""]]
        dict = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word not in dict:
                dict[sort_word] = [word]
            else:
                dict[sort_word].append(word)
        return [v for k,v in dict.items()]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


if __name__ == '__main__':
    unittest.main()
