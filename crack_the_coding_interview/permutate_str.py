"""base case and build"""

cnt = 0
def bruce_force(s, pre):
    if not s:
        print(pre)
        return

    for i in range(len(s)):
        bruce_force(s[:i]+s[i+1:], pre + s[i])


def base_case_and_build(s):
    res = ['']

    for c in s:
        tmp = []
        for sub in res:
            for i in range(len(sub)+1):
                tmp.append(sub[:i] + c + sub[i:])

        # res.extend(tmp)  # 包含不完全字串
        res = tmp  # 全字符串
    print(res)
    return res


if __name__ == '__main__':
    bruce_force('abcd', '')
    print('*' * 20)
    base_case_and_build('abcd')
