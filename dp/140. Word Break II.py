class Solution:
    def wordBreak(self, s: str, wordDict):

        self.words = wordDict
        self.ret = []

        def helper(s, container):
            # back
            if not s:
                self.ret.append(" ".join(container))
                return

            # process
            for word in self.words:
                if s.startswith(word):
                    # drill down
                    helper(s[len(word):], container + [word])

            # clear
            return self.ret

        return helper(s, [])