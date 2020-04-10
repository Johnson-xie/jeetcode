class Solution:
    def integerBreak(self, n: int) -> int:
        ##思路：n = 2,maxValue = 1;
        ###    n = 3,maxValue = 2 = max(1*2,2*1,1*1*1)
        ###    n = 4,maxValue = 4 =max(1*3,2*2,3*1,1*1*1*1)
        ###可以理解为，求n得最大乘积，转换成求1*(n-1),2*(n-2)....得最大乘积，也就是求（n-1）得最大乘积，（n-2）的最大乘积
        ###动态规划思路：如果我已经知道了：当n=1,n=2,n=3,n=4....的最大乘积，我接下来求n=k的乘积不就是编程max(（1*dp[n-1],2*dp[n-2].....k*dp)[n-k])）

        ##我们的目的时求出从2-——n的每个数的最大乘积，这样我求n的最大乘积不就是dp[n]即可
        ##第一步：初始化dp的个数，有n+1个，因为list的下标是从0开始，0-n,也就是n+1个数
        dp = [-1] * (n + 1)  ##当前每一个值都初始赋值为-1

        ##初始dp[2],因为我们已经知道2的最大乘积是1
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):  ##eg:如果当前这个i=n=3,那么，3的最大值，是不是应该从1*（3-1），2*（3-2）开始呢？ 1*1*1这种情况可以不考虑，因为它肯定是最小的始终为1，
                dp[i] = max(dp[i], j * (i - j), j * dp[
                    i - j])  ##同时要注意存在j*(i-j)为最大值的情况，所以也要考虑进去，以3为例，j*dp[i-j]:不就是求1*dp(2)，和2*dp[1]两个谁最大嘛?dp[2]我们已经知道是1。

        return dp[n]

    def integerBreak2(self, n: int) -> int:
        return n - 1 if n < 4 else 3**((n-2)//3) * ((n-2)%3+2)

"""
f(n) = f(n - 3) * 3 = f(n - 6) * 3 * 3 = f(n - 6) * 9
f(n) = f(n - 2) * 2 = f(n - 4) * 2 * 2 = f(n - 6) * 2 * 2 * 2 =f(n - 6) * 8
Therefore, when n is sufficiently large, 3 is always preferred.
"""