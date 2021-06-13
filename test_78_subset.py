import unittest

"""
write down thoughts
does not matter if nums are sorted or not, no duplicates, we are just enumerating all possible combinations
1. for loop
2. use backtrack to enumerate all combinations
"""

from typing import List


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         """for loop"""
#         res = []
#         res.append([])
#         for num in nums:
#             temp = []
#             for r in res: # for each result in result list, add new num
#                 tmp_r = r.copy()
#                 tmp_r.append(num)
#                 temp.append(tmp_r)
#             for t in temp:
#                 res.append(t)
#
#         return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """backtracking"""
        def backtrack(start, subset):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)  # create all combinations with subset, start combining with num[i+1]
                subset.pop()

        res = []
        backtrack(0, [])
        return res


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         cur = []
#         def dfs(i): # i to represent to include nums[i-1] or not
#             if i >=len(nums): # out of bound, NOT including the bound
#                 res.append(cur.copy())
#                 return
#
#             cur.append(nums[i]) # include nums[i]
#             dfs(i+1)
#
#             cur.pop() # not include nums[i]
#             dfs(i+1)
#         dfs(0)
#         return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[], [1], [2], [1, 2]], Solution().subsets([1, 2]))


if __name__ == '__main__':
    unittest.main()
