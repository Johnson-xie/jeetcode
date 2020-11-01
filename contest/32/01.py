class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        coins = self.count_change(s, t)
        k -= sum(coins)
        if k < 0:
            return False
        return k % 26 == 0

    def count_change(self, s, t):
        ret = []

        for i, j in zip(s, t):
            if j >= i:
                ret.append(ord(j) - ord(i))
            else:
                ret.append(26 - (ord(i) - ord(j)))
        print(ret)
        return ret


if __name__ == '__main__':
    s = "input"
    t = "ouput"
    k = 9
    sol = Solution()
    ret = sol.canConvertString(s, t, k)
    print(ret)
