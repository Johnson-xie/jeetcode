import bisect
import math


class Solution:
    staircase = []

    cur_high = 0
    for i in range(1, 2 ** 31):
        cur_high += i
        if cur_high > 2 ** 32:
            break
        staircase.append(cur_high)

    def arrangeCoins(self, n: int) -> int:
        return bisect.bisect_right(self.staircase, n)

    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1) / 2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.staircase)
