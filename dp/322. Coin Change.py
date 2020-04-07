class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memory = {}

        def helper(coins, amount):
            if amount in memory:
                return memory[amount]

            if amount == 0:
                memory[amount] = 0
                return 0

            res = float('inf')

            for coin in coins:
                if amount >= coin:
                    tmp_res = helper(coins, amount - coin)
                    if tmp_res == -1:
                        continue
                    else:
                        res = min(tmp_res + 1, res)
            if res == float('inf'):
                memory[amount] = -1
                return -1
            memory[amount] = res
            return res

        return helper(coins, amount)

    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
