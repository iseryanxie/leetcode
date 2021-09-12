import unittest

"""
write down thoughts
Use directions to indicate the movement in each direction. Use change_direction to track if there are need to change
directions in consecutive moves, which means it is the end because you can't go back or 
go around elements already visited.
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(matrix)
        columns = len(matrix[0])
        current_direction = 0
        # use 101 to denote it is visited because matrix elements are between -100 and 100
        VISITED = 101
        # track if we need to change directions two times in a row
        change_direction = 0
        row, col = 0, 0
        res = [matrix[row][col]]
        matrix[row][col] = VISITED
        while change_direction < 2:
            while True:  # keep going in one direction
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]
                if next_row >= rows or next_row < 0 or next_col >= columns or next_col < 0: # hit the boundary
                    break
                if matrix[next_row][next_col] == VISITED: # hit visited
                    break
                # reset change direction
                change_direction = 0
                row, col = next_row, next_col
                res.append(matrix[row][col])
                matrix[row][col] = VISITED

            # need to change direction because out of bounds or visited
            current_direction = (current_direction + 1) % 4  # there are four directions
            change_direction += 1
        return res


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual([1, 2, 3, 6, 9, 8, 7, 4, 5], Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


if __name__ == '__main__':
    unittest.main()
