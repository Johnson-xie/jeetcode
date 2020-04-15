class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        table = {(0, 0, 0, 0, 0): -1}

        a = 0
        e = 0
        i = 0
        o = 0
        u = 0

        max_length = 0

        for index, char in enumerate(s):
            if char == "a":
                a ^= 1
            elif char == "e":
                e ^= 1
            elif char == "i":
                i ^= 1
            elif char == "o":
                o ^= 1
            elif char == "u":
                u ^= 1

            ret = (a, e, i, o, u)
            if ret in table:
                max_length = max(max_length, index - table[ret])
            else:
                table[ret] = index

        return max_length
