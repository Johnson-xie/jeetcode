class Solution:
    def minFlips(self, target: str) -> int:
        target.lstrip('0')
        if not target:
            return 0

        status = [i for i in target.split('0') if i]

        return 2 * len(status) - 1


if __name__ == '__main__':
    s = '00000'
    ret = Solution().minFlips(s)
    print(ret)
