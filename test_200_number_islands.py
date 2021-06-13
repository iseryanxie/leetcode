class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == "1"):
                    num_islands += 1
                    self.checkNearby(grid, i, j)
        return num_islands

    def checkNearby(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])
        if i > rows - 1 or j > cols - 1 or i < 0 or j < 0 or grid[i][j] == "0":
            return
        if grid[i][j]=="1":
            grid[i][j] = "0"
            self.checkNearby(grid, i + 1, j)
            self.checkNearby(grid, i - 1, j)
            self.checkNearby(grid, i, j + 1)
            self.checkNearby(grid, i, j - 1)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "0", "0", "1"]
    ]
    ans = Solution().numIslands(grid)
    print(ans)
