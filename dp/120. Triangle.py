class Solution:
    def minimumTotal(self, triangle: "List[List[int]]") -> int:
        N = len(triangle)

        for row in range(N - 2, -1, -1):  # 倒数第二行开始

            for col in range(row + 1):
                triangle[row][col] = min(triangle[row + 1][col], triangle[row + 1][col + 1]) + triangle[row][col]

        return triangle[0][0]

    def minimumTotal2(self, triangle) -> int:



        if not triangle and not triangle[0]:
            return 0

        self.rows = len(triangle)

        self.cols = len(triangle)

        self._dfs(triangle, 0, 0, "", 0)

    def _dfs(self, triangle, row, col, path, _sum):

        # terminator
        if row == self.rows:
            print(path, "sum:", _sum)
            return _sum

        # process
        path += str(triangle[row][col]) + "--->"
        _sum += triangle[row][col]

        # drill down
        self._dfs(triangle, row + 1, col, path, _sum)
        self._dfs(triangle, row + 1, col + 1, path, _sum)

        # clear states
        return _sum

if __name__ == '__main__':
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    sol = Solution()
    sol.minimumTotal2(triangle)


"""
1. clarification
2. possible solutions
    brute force
    dp
3. coding
4. tests



"""
