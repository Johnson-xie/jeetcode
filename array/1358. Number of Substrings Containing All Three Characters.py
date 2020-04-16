import collections
import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        c = collections.Counter(t)

        c2 = copy.deepcopy(c)

        max_length = len(s)
        max_substring = s

        p1 = 0
        for p2 in range(len(s)):
            if s[p2] in c2:
                c2[s[p2]] += 1
                while not (c - c2):
                    if p2 - p1 + 1 < max_length:
                        max_length = p2 - p1 + 1
                        max_substring = s[p1: p2 + 1]

                    if s[p1] in c2:
                        c2[s[p1]] -= 1
                    p1 += 1

        return max_substring


S = "ADOBECODEBANC"
T = "ABC"
sol = Solution()
ret = sol.minWindow(S, T)