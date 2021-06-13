import unittest

"""
write down thoughts
First sort
1. for loop, based on 78, check if not duplicate, then add to res
2. backtracking/dfs, remove the case there is duplicate items
"""

from typing import List


# class Solution:
#     """for loop"""
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         res.append([])
#         for num in nums:
#             temp = []
#             for r in res:  # for each result in result list, add new num
#                 tmp_r = r.copy()
#                 tmp_r.append(num)
#                 temp.append(tmp_r)
#             for t in temp:
#                 if t not in res:
#                     res.append(t)
#
#         return res

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """backtracking"""

        def backtrack(start, subset):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)  # create all combinations with subset, start combining with num[i+1]
                subset.pop()

        nums.sort()  # need to sort
        res = []
        backtrack(0, [])
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[], [1], [1, 1], [1, 1, 2], [1, 2], [2]], Solution().subsetsWithDup([2, 1, 1]))


if __name__ == '__main__':
    unittest.main()
