class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(1, cols):
            grid[0][i] += grid[0][i - 1]

        for j in range(1, rows):
            grid[j][0] += grid[j - 1][0]

        for row in range(1, rows):
            for col in range(1, cols):
                left = grid[row][col - 1]
                up = grid[row - 1][col]
                grid[row][col] += min(left, up)

        return grid[-1][-1]