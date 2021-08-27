import math


def solution(n):
    answer = int(math.sqrt(n))
    if answer ** 2 != n:
        return -1
    return (answer+1) ** 2


if __name__ == "__main__":
    n = 5
    print(solution(n))
