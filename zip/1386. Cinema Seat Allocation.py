import collections


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        occupied = collections.defaultdict(int)
        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:
                occupied[seat[0]] |= (1 << (seat[1] - 2))
        print(occupied)
        ans = (n - len(occupied)) * 2
        for row, bitmask in occupied.items():
            if (bitmask | left) == left or (bitmask | middle) == middle or (bitmask | right) == right:
                ans += 1
        print(ans)
        return ans

    def maxNumberOfFamilies2(self, n: int, reservedSeats) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111

        occupied = collections.defaultdict(int)

        for row, value in reservedSeats:
            if 2 <= value <= 9:
                occupied[row] |= (1 << (value - 2))

        print(occupied)
        cnt = (n - len(occupied)) * 2
        for _, bitmask in occupied.items():
            if (bitmask | left) == left or (bitmask | middle) == middle or (bitmask | right) == right:

            # if (left | bitmask) == left or (middle | bitmask) == middle or (right | bitmask) == right:
                cnt += 1
        print(cnt)
        return cnt

if __name__ == '__main__':
    n = 3
    lst = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    sol = Solution()
    sol.maxNumberOfFamilies2(n, lst)
