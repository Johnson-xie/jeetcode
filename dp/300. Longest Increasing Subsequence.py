import bisect


class Solution:
    def lengthOfLIS(self, nums) -> int:
        nums.append(float('inf'))

        ret = [0] * len(nums)
        length = len(nums)

        fina_max = 1
        for i in range(length - 2, -1, -1):
            tmp_max = 1
            for j in range(i + 1, length):
                if nums[j] > nums[i]:
                    tmp_max = max(ret[j] + 1, tmp_max)
            ret[i] = tmp_max
            fina_max = max(tmp_max, fina_max)
        return fina_max

    def lengthOfLIS2(self, nums: List[int]) -> int:

        if not nums:
            return 0

        stack = []

        for num in nums:
            pos = bisect.bisect_left(stack, num)

            if len(stack) == pos:
                stack.append(num)
            else:
                stack[pos] = num

        return len(stack)

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    sol = Solution()
    ret = sol.lengthOfLIS(nums)
    print(ret)