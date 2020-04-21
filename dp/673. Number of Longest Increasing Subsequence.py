from functools import reduce
from itertools import product


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        ret = [1] * len(nums)

        for i in range(1, len(nums)):
            tmp_max = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp_max = max(ret[j] + 1, tmp_max)
            ret[i] = tmp_max

        return ret
if __name__ == '__main__':

    sol = Solution()
    ret = sol.findNumberOfLIS([1,2,4,3,5,4,7,2])
    print(ret)
    reduce