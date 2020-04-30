class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        cnt = 0

        self.x = [0, 0, -1, 1]
        self.y = [-1, 1, 0, 0]

        def dfs(x, y):
            if 0 <= x < rows and 0 <= y < cols:
                if grid[x][y] == '1':
                    grid[x][y] = 0
                    for dx, dy in zip(self.x, self.y):
                        dfs(x + dx, y + dy)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    cnt += 1
                    dfs(x, y)
        return cnt