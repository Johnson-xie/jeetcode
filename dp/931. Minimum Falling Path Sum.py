class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])

        for row in range(rows - 2, -1, -1):
            for col in range(0, cols):
                A[row][col] += min(A[row + 1][col], A[row + 1][col - 1] if col - 1 >= 0 else A[row + 1][col + 1],
                                   A[row + 1][col + 1] if col + 1 < cols else A[row + 1][col - 1])

        return min(A[0])

    def minFallingPathSum2(self, A):
        for i in range(1, len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i - 1][j and j - 1:j + 2])
        return min(A[-1])

if __name__ == '__main__':

    # A= [[1,2,3],[4,5,6],[7,8,9]]
    A= [[51,24],[-50,82]]
    sol = Solution()
    ret = sol.minFallingPathSum(A)
    print(ret)
