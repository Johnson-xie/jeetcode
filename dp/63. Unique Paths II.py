class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        for row in range(n):
            for col in range(m):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                elif row == 0 and col == 0:
                    obstacleGrid[row][col] = 1
                else:
                    left = obstacleGrid[row][col - 1] if col - 1 >= 0 else 0
                    up = obstacleGrid[row - 1][col] if row - 1 >= 0 else 0
                    obstacleGrid[row][col] = left + up

        return obstacleGrid[-1][-1]


a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
sol = Solution()
ret = sol.uniquePathsWithObstacles(a)
