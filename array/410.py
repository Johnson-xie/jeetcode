class Solution:
    def splitArray(self, nums, m: int) -> int:
        self.nums = nums
        self.min_value = float('inf')
        insert = m - 1
        self.help(insert, [])
        return self.min_value

    def help(self, m, sep):
        if m == 0:
            self.min_value = min(self.min_value, self.cut(sep))
            return

        for index in range(1, len(self.nums)):
            self.help(m - 1, sep + [index])

    def cut(self, sep):
        sep = [0] + sep + [10001]
        max_value = -1
        for first, end in zip(sep, sep[1:]):
            max_value = max(max_value, sum(self.nums[first: end]))
        return max_value


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    ret = Solution().splitArray(nums, m)
    print(ret)
