import collections

"""滑动窗口缓存"""


def calculate_s1_per_in_s2(s1, s2):
    length_s1, length_s2 = len(s1), len(s2)
    if length_s1 > length_s2:
        return 0

    cnt = 0

    cache = collections.defaultdict(int)
    for c in s1:
        cache[c] += 1

    windows = collections.defaultdict(int)
    for c in range(length_s1):
        windows[s2[c]] += 1

    for i in range(length_s1, length_s2):
        if windows == cache:
            cnt += 1
        windows[s2[i - length_s1]] -= 1
        if windows[s2[i - length_s1]] == 0:
            windows.pop(s2[i - length_s1])
        windows[s2[i]] += 1
    else:
        if windows == cache:
            cnt += 1

    print(cnt)
    return cnt


if __name__ == '__main__':
    s = 'abbc'
    b = 'cbabadcbbabbcbabaabccbabc'
    calculate_s1_per_in_s2(s, b)
