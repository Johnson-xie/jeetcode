class Solution:
    def findMaxLength(self, nums) -> int:
        sub_table = {}
        max_length = 0
        cnt = 0

        for index, num in enumerate([0] + nums):  # 开始的时候一样多，都没有
            if num == 0:
                cnt += 1
            else:
                cnt -= 1
            if cnt not in sub_table:
                sub_table[cnt] = index
            else:
                max_length = max(max_length, index - sub_table[cnt])

        return max_length


if __name__ == '__main__':
    nums = [0, 1]

