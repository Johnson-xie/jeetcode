class Solution:
    def findString(self, words, s) -> int:
        first, last = 0, len(words) - 1
        self.words = words
        self.s = s
        return self.binary_search(first, last) or -1

    def binary_search(self, first, last):
        while first <= last:
            mid = (first + last) // 2
            if self.words[mid] == self.s:
                return mid
            elif self.words[mid] == "":
                return self.binary_search(first, mid - 1) or self.binary_search(mid + 1, last)
            elif self.words[mid] > self.s:
                last = mid - 1
            elif self.words[mid] < self.s:
                first = mid + 1


if __name__ == '__main__':
    words = ["GEHHrM", "IZC", "JZqYk aIZu ", "U", "YhwFkkXaUcp", "ogXjJxZIgrgTzHzpsh", "xUVITUdTNTFBWJ",
             "yoNDXSRrzKLwXQpV"]
    s = "GEHHrM"
    ret = Solution().findString(words, s)
    print(ret)
