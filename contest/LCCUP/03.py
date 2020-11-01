import re

leaves = "rrryrryyyrr"
# leaves = "yyyyyyyyyy"
# leaves = 'ryr'


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        extro = 0
        if leaves[0] != 'r' and leaves[-1] != 'r':
            extro += 2
            leaves = 'r' + leaves[1:-1] + 'r'
        elif leaves[0] != 'r':
            extro += 1
            leaves = 'r' + leaves[1:]
        elif leaves[-1] != 'r':
            extro += 1
            leaves = leaves[:-1] + 'r'

        if len(set(leaves)) == 1:
            return 1 + extro

        left = 0
        for i in range(1, len(leaves)):
            if leaves[i] != 'r':
                left = i
                break
        right = len(leaves) - 1
        for i in range(len(leaves) - 2, -1, -1):
            if leaves[i] != 'r':
                right = i
                break

        return sum(c == 'r' for c in leaves[left:right + 1]) + extro


if __name__ == '__main__':
    ret = Solution().minimumOperations(leaves)
    print(ret)
