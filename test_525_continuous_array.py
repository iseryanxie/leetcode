import unittest
import bisect

"""
write down thoughts
1. calc cum sum, for each 0, decrement -1
2. calc cum sum, for each 1, increment 1
3. create a hashmap to record the first time of the cum sum has recorded
4. if cum sum is already in hashmap, max length = max(maxlen, i-hashmap[cum_sum])
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen, cum_sum = 0, 0
        hashmap = {}
        for i, num in enumerate(nums):
            if num == 0:
                cum_sum -= 1
            else:
                cum_sum += 1
            if cum_sum == 0:
                maxlen = max(maxlen, i + 1)
            if cum_sum in hashmap:
                maxlen = max(maxlen, i - hashmap[cum_sum])
            else:
                hashmap[cum_sum] = i

        return maxlen


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, Solution().findMaxLength([0, 1, 0]))

    def test2(self):
        self.assertEqual(14, Solution().findMaxLength([0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0]))


if __name__ == '__main__':
    unittest.main()
