import bisect


class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

    def nextGreatestLetter2(self, letters, target: str) -> str:
        index = bisect.bisect_right(letters, target)
        return letters[index % len(letters)]

    def nextGreatestLetter3(self, letters, target: str) -> str:
        s = set(letters)

        for i in range(1, 27):
            next = chr(ord(target) + i)
            if next in s:
                return next

        return letters[0]
if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "c"
    sol = Solution()
    ret = sol.nextGreatestLetter3(letters, target)
    print(ret)
