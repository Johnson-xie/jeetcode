class Solution:
    def pivotIndex(self, nums) -> int:
        s = sum(nums)

        for index in range(0, len(nums)):
            sub = s - nums[index]
            if not (sub & 1):
                if sum(nums[: index]) == sub / 2:
                    return index

        return -1

    def pivotIndex2(self, nums) -> int:
        s = sum(nums)

        cur_sum = 0
        for index in range(0, len(nums)):
            sub = s - nums[index]
            if cur_sum == sub / 2:
                return index
            cur_sum += nums[index]

        return -1

    def pivotIndex3(self, nums) -> int:
        s = sum(nums)

        cur_sum = 0
        for index in range(0, len(nums)):
            sub = s - nums[index]
            if cur_sum == sub / 2:
                return index
            cur_sum += nums[index]

        return -1


if __name__ == '__main__':
    nums = [-1,-1,-1,0,1,1]
    sol = Solution()
    ret = sol.pivotIndex2(nums)
    print(ret)