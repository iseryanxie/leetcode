import unittest

"""
write down thoughts
rotate in groups, first start with four corners, then the ones next to the corner, all the way towards to center
note that the rotation happens like this, for example r=0,c=1 [0,1]->[1,n-1-0]->[n-1-0][n-1-1]->[n-1-1][0]
to generalize [r,c]->[c][n-1-r]->[n-1-r][n-1-c]->[n-1-c][r]
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for r in range(n//2+n%2):  # r is row, from 0 to center
            for c in range(n//2):
                # for middle column (if n%2==1), skip when rotating columns, this will be handled by the extra n%2
                # in rows operation
                tmp = matrix[n-1-c][r]
                matrix[n-1-c][r] = matrix[n-1-r][n-1-c]
                matrix[n-1-r][n-1-c] = matrix[c][n-1-r]
                matrix[c][n-1-r] = matrix[r][c]
                matrix[r][c] = tmp



class TestSolution(unittest.TestCase):
    def test1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Solution().rotate(matrix)
        self.assertEqual([[7, 4, 1], [8, 5, 2], [9, 6, 3]], matrix)


if __name__ == '__main__':
    unittest.main()
