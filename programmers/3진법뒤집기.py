import sys
input = sys.stdin.readline


def solution(n):
    temp = []
    answer = 0

    while n != 0:
        temp.insert(0, n % 3)
        n = n // 3

    print(temp)
    for idx, i in enumerate(temp):
        answer += i * (3 ** idx)
    return answer


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
