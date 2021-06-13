import unittest
import bisect

"""
write down thoughts
Approach 1
sort then return the k largest
Approach 2
A variation of quicksort: quick select, O(n)
1. random choose pivot point, partition list into 3 lists, <,==,>
2. if |left|>k, then find Kth largest in left list, recursion
3, if |left|+|mid|<k, find (k-|left|-|mid|) largest in right list, recursion
4. else return mid[0]
"""
from typing import List


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if k>len(nums) or k<1:
#             return 0
#         # nums.sort(reverse=True)
#         # return nums[k-1]
#         nums.sort()
#         return nums[-k]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)
        if k <= L:  # left list has more than k elements
            return self.findKthLargest(left, k)  # search in the left
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))


if __name__ == '__main__':
    unittest.main()
