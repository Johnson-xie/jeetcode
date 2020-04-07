class Solution:
    def countBits(self, num: int):
        dp = [0] * (num + 1)

        for i in range(1, num + 1):
            dp[i] += dp[i & (i - 1)] + 1

        # i这个数肯定比 i & (i - 1)这个数多一个1
        # 利用i作为索引，得出转移方程

        # 而i & (i - 1)肯定已经得出了有多少个1

        """        打掉末位1，注意不是减去1
        0     0       
        1     1    00 ---> 0
        2    10    00 ---> 0
        3    11    10 ---> 2
        4   100    11 ---> 3
        5   101   100 ---> 4
        6   110   100 ---> 4
        
        """

        return dp

