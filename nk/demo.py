# s1 = input()
# s2 = input()
def f1():
    s1 = "oswgkjwvstbgfzszdoemlpvtoqeautekdfwpezdfxatvcyskrisiqcjynmtwcfmzzuseyaxanc"
    s2 = "guwldvzrsfurobidegiyazkggfpgmyhlrbfjrjerrbnjdenrdxjfmrhtumfdsedkcmthphgavzxlmpcpwbkwsvplhmkbkgkw"
    print(len(s1), len(s2))
    n1 = 8 - (len(s1) % 8) if (len(s1) % 8) else 0
    n2 = 8 - (len(s2) % 8) if (len(s2) % 8) else 0
    print(n1, n2)
    print(len(s1), len(s2))
    s = s1 + "0" * n1 + s2 + "0" * n2
    for i in range(0, len(s), 8):
        print(s[i: i + 8])


def f2():
    n = 65477
    nums = []

    num = 2
    while n != 1:
        if n % num == 0:
            n /= num
            nums.append(str(num))
        else:
            num += 1

    print(" ".join(nums) + " ")

def f3():
    while True:
        try:
            n = float(input())
            print(math.ceil(n))
        except:
            pass

def f4():
    n = int(input())

    ret = {}

    for i in range(n):
        key, value = input().split(' ')
        if key in ret:
            ret[key] += int(value)
        else:
            ret[key] = int(value)
    for key in sorted(ret.keys()):
        print(key, " ", ret[key])


def f5():
    n = input()

    return len({i for i in n if 0 <= ord(i) <= 127})

def f6():
    print(" ".join(input().split(" ")[::-1]))


def f7():
    try:
        n = int(input)
        ret = []
        for i in range(n):
            s = input()
            ret.append(s)

        for i in sorted(ret):
            print(i)
    except:
        pass

def f8():
    lst = [1000, 1200, 1500, 2000, 1600]
    

if __name__ == '__main__':
    f7()

