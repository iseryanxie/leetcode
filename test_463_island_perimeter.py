import unittest

"""
write down thoughts
for each 1, there are 4 sides to count. However, if there are adjacent cells also is land, then -2.
For each cell, only check left and above, because it will eventually be checked at the lower right corner.
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == 0:
                    continue
                perimeter += 4
                if col_index>=1 and grid[row_index][col_index-1]:
                    perimeter -=2
                if row_index>=1 and grid[row_index-1][col_index]:
                    perimeter -=2
        return perimeter


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(16, Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))


if __name__ == '__main__':
    unittest.main()
