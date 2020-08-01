import itertools

from scipy.special import comb


class Solution:
    def numOfSubarrays(self, arr) -> int:
        cnt = 0

        for i in range(len(arr)):
            accumulate_sum = 0
            for j in range(i, len(arr)):
                accumulate_sum += arr[j]
                if accumulate_sum % 2:
                    cnt += 1

        return cnt


if __name__ == '__main__':
    arr = [64,69,7,78,31,83,47,84,47,6,67]
    ret = Solution().numOfSubarrays(arr)
    print(ret)
