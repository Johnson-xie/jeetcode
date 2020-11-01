import bisect
import collections
import itertools


class Solution:
    def breakfastNumber(self, staple, drinks, x: int) -> int:
        cnt = 0

        staple_map = collections.Counter(staple).items()

        drinks_map = sorted(collections.Counter(drinks).items(), key=lambda x: x[0])
        drinks_list = [key for key, _ in drinks_map]
        drinks_value = list(itertools.accumulate([val for _, val in drinks_map]))
        # drinks_map = collections.Counter(drinks)

        for i, val1 in staple_map:
            if i >= x:
                continue
            left = x - i
            p = bisect.bisect_right(drinks_list, left)
            if p == 0:
                continue
            cnt += val1 * drinks_value[p - 1]

        return cnt % 1000000007


if __name__ == '__main__':
    staple = [2, 1, 1]
    drinks = [8, 9, 5, 1]
    x = 9
    # staple = [10, 20, 5]
    # drinks = [5, 5, 2]
    # x = 15
    ret = Solution().breakfastNumber(staple, drinks, x)
    print(ret)
