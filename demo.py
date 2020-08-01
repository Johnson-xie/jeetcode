import math


class Solution:
    def minDifference(self, nums) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        n1 = nums[3:]
        n2 = nums[:-3]
        n3 = nums[2:-1]
        n4 = nums[1:-2]
        return min(n1[-1] - n1[0], n2[-1] - n2[0], n3[-1] - n3[0], n3[-1] - n3[0])


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        elif n == 2:
            return False

        dp = [False] + [None for i in range(n)]

        dp[1], dp[2] = [True, False]

        for nth in range(3, n + 1):
            # 递推，获取局部最优解，第n个数谁会赢，n+1由n得出
            for num in range(1, int(math.sqrt(nth)) + 1):
                """
                第三个，找一个大于1小于n的数(1<num<n),且能被n整除的数，枚举所有，如果减去之后dp[n - num]为False,那么就能赢
                dp[n]就设置为True
                否者设置为False

                """
                if dp[nth - num**2] == False:
                    dp[nth] = True
                    break
            else:
                dp[nth] = False
        return dp[-1]

if __name__ == '__main__':
    nums = 3
    res = Solution().winnerSquareGame(nums)
    print(res)