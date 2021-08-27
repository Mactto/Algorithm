def solution(n):
    count = 0
    while n != 1:
        count += 1
        if 500 < count:
            return -1
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    return count


if __name__ == "__main__":
    n = 6
    print(solution(n))
