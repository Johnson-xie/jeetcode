class Solution:
    def minCost(self, s: str, cost) -> int:
        if len(s) == 1:
            return 0

        ret_list = []
        ret_sum = 0

        start = 0
        for i in range(1, len(s)):
            if s[i] == s[start]:
                continue
            else:
                if i - start > 1:
                    ret_list.append((start, i - 1))
                start = i
        else:
            if len(s) - 1 != start and s[-1] == s[start]:
                ret_list.append((start, len(s) - 1))

        for start, end in ret_list:
            tmp = [cost[i] for i in range(start, end + 1)]
            ret_sum += sum(tmp) - min(tmp)

        return ret_sum


if __name__ == '__main__':
    s = "abaac"
    cost = [1, 2, 3, 4, 5]
    ret = Solution().minCost(s, cost)
    print(ret)







