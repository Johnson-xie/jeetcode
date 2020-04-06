class Solution:
    def minCostClimbingStairs(self, cost: "List[int]") -> int:
        dp = [0, 0] + cost
        dp.append(0)

        """
        过程是经过当前节点的耗费，由前面两个阶梯决定， 最终要到达终点

        0，0，c1, c2, ....   cn, 0

        c1 = min(dp[c1 - 1], dp[c1 - 2]) + c1


        """

        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + dp[i]

        return dp[-1]



    def minCostClimbingStairs2(self, cost: "List[int]") -> int:
        if not cost:
            return 0

        if len(cost) == 2:
            return min(cost)

        dp = [0] + cost + [0]

        self.cache = {}  # 做缓存


        def helper(n):
            if n == 1:
                return dp[1]
            elif n == 2:
                return dp[2]
            else:
                if n in self.cache:
                    return self.cache[n]
                else:
                    ret = min(helper(n - 1), helper(n - 2)) + dp[n]
                self.cache[n] = ret
                return ret

        return helper(len(dp) - 1)


    def minCostClimbingStairs3(self, cost):

        # lee神
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2:])


if __name__ == '__main__':

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    ret = sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(ret)
