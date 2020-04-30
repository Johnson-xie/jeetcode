class Solution:
    def stringShift(self, s: str, shift) -> str:
        left, right = 0, 0
        for direction, step in shift:
            if direction == 0:
                left += step
            else:
                right += step

        flag = True if left - right > 0 else False
        step = abs(left - right) % len(s)
        if step == 0:
            return s

        return s[step:] + s[:step] if flag else s[-step:] + s[:len(s) - step]


if __name__ == '__main__':
    s = "joiazl"
    ss = [[1, 1], [1, 6], [0, 1], [1, 3], [1, 0], [0, 3]]
    sol = Solution()
    ret = sol.stringShift(s, ss)
    print(ret)