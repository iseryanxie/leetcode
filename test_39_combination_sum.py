import unittest

"""
write down thoughts
method 1: dfs
1. in each decision point, we define a decision to include a number (the combination can have the number in it) or 
not include a number (that number is not allowed at all in the remaining combinations).
2. then recursively call the function
method 2: dp
faster with more memory consumption
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        #
        # def dfs(i, curr, total):  # i is the index of the number to include or not
        #     if i >= len(candidates) or total > target:  # no longer a valid branch
        #         return
        #     if total == target:
        #         res.append(curr.copy())
        #         return
        #
        #     curr.append(candidates[i])
        #     # index is still i, because on the branch to include i, it can have more than 1 i.
        #     dfs(i, curr, total + candidates[i])
        #     curr.pop()
        #     dfs(i + 1, curr, total)
        #
        # dfs(0, [], 0)
        # return res
        dp = [[] for _ in range(target + 1)]
        for c in candidates:  # for each candidate as a row
            for i in range(1, target + 1):
                if i < c:
                    # not possible, because candidate is larger than remaining sum
                    continue
                if i == c:
                    # add c to the dp list
                    dp[i].append([c])
                else:
                    for blist in dp[i - c]:
                        # for each possible combination (each is a list of numbers to attain dp[i-c])
                        dp[i].append(blist + [c])  # extend the list to include c that will make i-c become i
        return dp[target]


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([[2, 2, 3], [7]], Solution().combinationSum([2, 3, 6, 7], 7))

    def test2(self):
        self.assertEqual([[2, 2, 2, 2], [2, 3, 3], [3, 5]], Solution().combinationSum([2, 3, 5], 8))


if __name__ == '__main__':
    unittest.main()
