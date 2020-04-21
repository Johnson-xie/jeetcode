class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        max_inc = 1

        if len(nums) <= 1:
            return len(nums)

        cur_inc = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                cur_inc += 1
            else:
                max_inc = max(cur_inc, max_inc)
                cur_inc = 1

        return max(cur_inc, max_inc)

if __name__ == '__main__':
    sol = Solution()
    ret = sol.findLengthOfLCIS([1,3,5,7])
    print(ret)
