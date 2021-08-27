import sys
input = sys.stdin.readline


def solution(n):
    if n % 2 == 0:
        return "수박" * (n // 2)
    else:
        return ("수박" * (n // 2)) + "수"


if __name__ == "__main__":
    n = 5
    print(solution(n))
