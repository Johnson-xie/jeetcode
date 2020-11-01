def find_common(A, B):
    length_A, length_B = len(A), len(B)

    ret, i, j = [], 0, 0

    while i < length_A and j < length_B:
        if A[i] == B[j]:
            ret.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
    print(ret)
    return ret


if __name__ == '__main__':
    A = [13, 27, 35, 40, 49, 55, 59]
    B = [17, 35, 39, 40, 55, 58, 60]
    find_common(A, B)
