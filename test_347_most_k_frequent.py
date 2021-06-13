import unittest
import bisect

"""
write down thoughts
"""
from typing import List


# class Solution:
#
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         from collections import Counter
#         cnt_k = Counter(nums).most_common(k)
#         return [x[0] for x in cnt_k]
#

# class Solution:
#
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = {}
#         for num in nums:
#             if num not in freq:
#                 freq[num] = 1
#             else:
#                 freq[num] += 1
#         freq=sorted(freq.items(),key=lambda x: x[1],reverse=True) # must replace freq, sorted does not operate inplace
#         return [x[0] for x in freq[0:k]]

class Solution:
    # heap implementation is the fastest
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        d = Counter(nums)
        heap = []
        for key, val in d.items():
            if len(heap) == k: # if already k elements, push then pop the smallest in the heap
                # (so it's always the largest K in the heap)
                heapq.heappushpop(heap, (val,key))
            else:
                heapq.heappush(heap, (val,key))
        heap.sort(reverse=True) # optional, only needed to pass leetcode checks
        return [y for x,y in heap]

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([1, 2], Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()
