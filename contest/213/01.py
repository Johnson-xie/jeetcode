class Solution:
    def countVowelStrings(self, n: int) -> int:
        return sum(i**(n-1) for i in range(1, 6))


if __name__ == '__main__':
    print(Solution().countVowelStrings(3))
