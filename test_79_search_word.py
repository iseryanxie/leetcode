import unittest

"""
write down thoughts
similar to problem walk maze
use dfs to search
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, d):  # search at coordinate(x,y) for char word[d]
            if x < 0 or x == len(board[0]) or y < 0 or y == len(board): return False
            if board[y][x] != word[d]: return False
            if d == len(word) - 1: return True  # exhausted the word string

            # in order to avoid duplicate search the current location, save the char and block the search for current
            # position
            cur = board[y][x]
            board[y][x] = ""
            found = dfs(x - 1, y, d + 1) or dfs(x + 1, y, d + 1) or dfs(x, y - 1, d + 1) or dfs(x, y + 1, d + 1)
            # after dfs, restore char
            board[y][x] = cur
            return found

        # for each position as starting point, dfs search
        for i in range(len(board[0])):
            for j in range(len(board)):
                if dfs(i, j, 0): return True
        return False


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))
    def test2(self):
        self.assertEqual(True,
                         Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    def test3(self):
        self.assertEqual(False,
                         Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))



# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

if __name__ == '__main__':

    unittest.main()
