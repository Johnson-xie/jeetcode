import math


class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        elif N == 2:
            return True

        dp = [None] + [None for i in range(N)]

        dp[1], dp[2] = [False, True]

        for nth in range(1, N + 1):
            # 递推，获取局部最优解，第n个数谁会赢，n+1由n得出
            for num in range(1, nth // + 1):
                """
                首先1肯定输，直接动不了
                
                2，拿一个变为1，拿一个后结果为False,2能赢
                
                第三个，找一个大于1小于n的数(1<num<n),且能被n整除的数，枚举所有，如果减去之后dp[n - num]为False,那么就能赢
                
                
                dp[n]就设置为True
                否者设置为False
                
                """
                if nth % num == 0 and dp[nth - num] == False:
                    dp[nth] = True
                    break
            else:
                dp[nth] = False
        return dp[-1]

    def divisorGame2(self, N: int) -> bool:
        """偶数就能赢"""
        return N % 2 == 0


class Solution2:
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
                if dp[nth - num ** 2] == False:
                    dp[nth] = True
                    break
            else:
                dp[nth] = False
        return dp[-1]
