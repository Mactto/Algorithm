def convert(n, q):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, q)
    if q == 0:
        return arr[r]
    else:
        return convert(q, q) + arr[r]


def solution(n, t, m, p):
    result = '0'
    temp = 1

    while len(result) < t * m * p:
        result += convert(temp, n)
        temp += 1
    return result[p-1::m][:t]


if __name__ == "__main__":
    print(solution(16, 16, 2, 1))
