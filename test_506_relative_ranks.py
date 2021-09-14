import unittest

"""
write down thoughts
Sort the list, because each rank is needed. Use a hashmap to find the corresponding place with the score (score is unique)
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sorted = sorted(score, reverse=True)
        map = {}
        for i in range(len(score_sorted)):
            if i == 0:
                map[score_sorted[i]] = "Gold Medal"
            elif i == 1:
                map[score_sorted[i]] = "Silver Medal"
            elif i == 2:
                map[score_sorted[i]] = "Bronze Medal"
            else:
                map[score_sorted[i]] = str(i+1)

        return [map[i] for i in score]

class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(["Gold Medal","Silver Medal","Bronze Medal","4","5"], Solution().findRelativeRanks([5,4,3,2,1]))


if __name__ == '__main__':
    unittest.main()
