import collections

"""哈希缓存"""
def power3(n):
    cache = collections.defaultdict(list)

    for a in range(1, n+1):
        for b in range(a, n+1):
            cache[a**3 + b**3].append((a, b))

    for values in cache.values():
        if len(values) > 1:
            print_combination(values)


def print_combination(lst):
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            print(lst[i], lst[j])
            # cube1 = lst[i][0]**3 + lst[i][1]**3
            # print('%s^3 + %s^3=%s' % (lst[i][0], lst[i][1],cube1))
            # cube2 = lst[j][0]**3 + lst[j][1]**3
            # print('%s^3 + %s^3=%s' % (lst[j][0], lst[j][1],cube2))
            # print("*" * 20)


if __name__ == '__main__':
    power3(1000)
