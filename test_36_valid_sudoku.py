import unittest

"""
write down thoughts
1. only validate existing numbers
2. for each row/col/box, keep a hashset to store the occurred numbers, if found duplicate, then False.
"""

from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # index is a tuple of (i//3,j//3)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue  # only validate numbers
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i // 3, j // 3)]:
                    # for boxes, 0-2 is mapped to 0, 3-5 ->2, 6-98 -> 3.
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i // 3, j // 3)].add(board[i][j])
        return True


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))


if __name__ == '__main__':
    unittest.main()
