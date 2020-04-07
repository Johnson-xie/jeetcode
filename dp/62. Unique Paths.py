class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        self.memory = {}

        def helper(m, n):
            if m == 1 or n == 1:
                return 1
            else:
                if (m, n) in self.memory:
                    ret = self.memory[(m, n)]
                else:
                    ret = helper(m - 1, n) + helper(m, n - 1)
                    self.memory[(m, n)] = ret
                return ret

        return helper(m, n)


    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[0] * m for i in range(n)]
        dp[0] = [1] * m

        for i in range(n):
            dp[i][0] = 1

        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[-1][-1]
