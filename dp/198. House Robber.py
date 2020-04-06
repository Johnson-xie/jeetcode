class Solution:
    def rob(self, nums) -> int:
        dp = [0, 0] + nums

        for i in range(2, len(dp)):
            dp[i] = max(dp[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

    def rob2(self, nums: List[int]) -> int:
        pre, cur = 0, 0

        for num in nums:
            pre, cur = cur, max(num + pre, cur)
        return cur

if __name__ == '__main__':
    nums = [2, 1, 1, 2]
    sol = Solution()
    ret = sol.rob2(nums)

    print(ret)
