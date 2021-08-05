import unittest

"""
write down thoughts
Use backtrack
1. sort
2. to the left, is to use that number, to the right is to not use that number.
3. when the branch is to use that number, the number can be used multiple times (as long as there are multiple 
occurrences in the candidate set).
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target < 0:
                return
            prev = -1
            for i in range(pos, len(candidates)):  # consider only the numbers to the right of the position
                if candidates[i] == prev:  # skip the number that is duplicated
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                # when the new candidate is added, start the search from the position+1, note that prev is reset to
                # make sure 1,1,6 is possible, but 1,7 is unique.
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([
            [1, 1, 6],
            [1, 2, 5],
            [1, 7],
            [2, 6]
        ], Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))


if __name__ == '__main__':
    unittest.main()
