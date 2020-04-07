class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        for row in range(N - 2, -1, -1):  # 倒数第二行开始

            for col in range(row + 1):
                triangle[row][col] = min(triangle[row + 1][col], triangle[row + 1][col + 1]) + triangle[row][col]

        return triangle[0][0]

