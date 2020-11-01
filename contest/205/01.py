import random


class Solution:
    def modifyString(self, s: str) -> str:

        def get_chr(occupy):
            num = random.randint(97, 122)
            while True:
                if num not in occupy:
                    return chr(num)
                num = random.randint(97, 122)

        s_list = ['?'] + list(s) + ['?']

        for index in range(1, len(s_list) - 1):
            if s_list[index] != '?':
                continue

            ret = {(ord(s_list[index - 1])), ord(s_list[index + 1])}
            s_list[index] = get_chr(ret)

        return ''.join(s_list[1:len(s_list) - 1])


if __name__ == '__main__':
    ret = Solution().modifyString("?s??")
    print(ret)




