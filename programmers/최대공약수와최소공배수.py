def solution(n, m):
    gcd, lcm = 0, 0
    temp = 1

    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    while True:
        value = max(n, m) * temp
        if value % min(n, m) == 0:
            lcm = value
            break
        temp += 1
    return [gcd, lcm]


if __name__ == "__main__":
    n = 2
    m = 5
    print(solution(n, m))
