class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        wordDict = set(wordDict)

        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

                    # 直接可以中断返回
                    if j == n + 1:
                        return True

        return dp[-1]

"""缓存： 所有有return的地方都要加"""
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.cache = {}
        self.words = set(wordDict)
        self.end = len(s)

        def search(s, i):

            if i in self.cache:
                return self.cache[i]

            # back point
            if i == self.end:
                self.cache[i] = True
                return True

            # process
            for word in wordDict:
                if s[i: i + len(word)] in self.words and search(s, i + len(word)):
                    # dirll down
                    self.cache[i] = True
                    return True

            # clear
            self.cache[i] = False
            return False

        return search(s, 0)


