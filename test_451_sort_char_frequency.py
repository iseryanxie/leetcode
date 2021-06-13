import unittest
import bisect

"""
write down thoughts
Use bucket sort, achieve O(n)
1. count and add to dictionary
2. create bucket (list of list) with len(s), key is the frequency, value is the char
3. add char to bucket of corresponding frequency slot
4. enumerate from top to low and add to res string
"""


class Solution(object):
    def frequencySort(self, s: str) -> str:
        # Counter is ordered by frequency
        # from collections import Counter
        # freq_map = Counter(s)
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 1
            else:
                freq_map[char] += 1

        bucket = [[] for _ in range(len(s)+1)]
        for c,v in freq_map.items():
            bucket[v].append(c)
        res = ""
        for i in range(len(s),0,-1): # at most len(s) times, from most frequent to least frequent
            for c in bucket[i]: # bucket[i] can be 0
                for r in range(i):
                    res += c
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual("eetr", Solution().frequencySort("tree"))


if __name__ == '__main__':
    unittest.main()
