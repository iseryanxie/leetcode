import unittest
import bisect

"""
write down thoughts
"""
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        from collections import Counter
        cnt_map = Counter(words).most_common(k)
        return [x[0] for x in cnt_map]
#
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         d = {}
#
#         words.sort()
#
#         for word in words:
#             if word in d:
#                 d[word] += 1
#             elif word not in d:
#                 d[word] = 1
#
#         ll = sorted(d, key=lambda x: d[x], reverse=True)
#
#         return ll[0:k]

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["i", "love"], Solution().topKFrequent(["me","i", "love", "leetcode", "i", "love", "coding"], 2))


if __name__ == '__main__':
    unittest.main()
