class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        cols = len(A) + 1
        rows = len(B) + 1

        dp = [[0] * cols for row in range(rows)]
        max_length = dp[0][0]
        for row in range(1, rows):
            for col in range(1, rows):
                if A[col - 1] == B[row - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                    max_length = max(max_length, dp[row][col])

        return max_length


# dp[i][j]表示以该字符结尾的连续子串长度是多少