class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1) - 1, len(num2) - 1

        cur, adv = 0, 0
        nums = []

        while N1 >= 0 and N2 >= 0:
            adv, cur = divmod(int(num1[N1]) + int(num2[N2]) + adv, 10)
            nums.append(str(cur))
            N1 -= 1
            N2 -= 1
        while N1 >= 0:
            adv, cur = divmod(int(num1[N1]) + adv, 10)
            nums.append(str(cur))
            N1 -= 1
        while N2 >= 0:
            adv, cur = divmod(int(num2[N2]) + adv, 10)
            nums.append(str(cur))
            N2 -= 1
        if adv:
            nums.append(str(adv))
        return "".join(reversed(nums))

ret = Solution().addStrings("9", "99")
print(ret)