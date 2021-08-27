def solution(n):
    n = list(str(n))
    return list(map(int, n[::-1]))


if __name__ == "__main__":
    n = 12345
    print(solution(n))
