import unittest
from typing import List
from collections import Counter
import bisect
"""
write down thoughts
1. write a function that returns the occurance of lexicographically smallest char
2. Convert both queries and words with the function above, which results in list of number
3. sort the list from words
4. use bisect to quickly find how many words has f(word)<f(query)
"""


class Solution:
    def freq_smallest_char(self, s: str):
        """function to return the frequency of the smallest char in the string"""
        s_count = Counter(s)
        return s_count[min(s_count.keys())]  # min function returns the lexicographically smallest chars

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query_count = map(self.freq_smallest_char, queries)
        word_count = sorted(map(self.freq_smallest_char, words))
        ans = []
        for query in query_count:
            ans.append(len(word_count)-bisect.bisect(word_count,query))
            # find how many f(words)>f(queries) use len()-numbers less than word
            # use bisect_right/bisect to filter <= and keep > only
        return ans


class TestSolution(unittest.TestCase):
    def test1(self):
        queries = ["cbd"]
        words = ["zaaaz"]
        self.assertEqual([1], Solution().numSmallerByFrequency(queries, words))
    def test2(self):
        queries = ["cbd"]
        words = ["zaaaz","a","b"]
        self.assertEqual([1], Solution().numSmallerByFrequency(queries, words))


if __name__ == '__main__':
    unittest.main()
