class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        N = len(A)
        cnt = 1
        start = 0

        for i in range(1, N):
            diff = A[i - 1] - A[i]
            if diff == 0:
                start = i
            elif i == N - 1 or diff * (A[i] - A[i + 1]) >= 0:
                cnt = max(cnt, i - start + 1)
                start = i
        return cnt


if __name__ == '__main__':
    sol = Solution()
    A = [9,4,2,10,7,8,8,1,9]
    ret = sol.maxTurbulenceSize(A)
    print(ret)
