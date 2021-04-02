import sys
input = sys.stdin.readline

def algorithm():
    start = 1
    end = M
    distance = 0

    for _ in range(j):
        p = int(input())

        if p < start:
            distance += (start - p)
            start = p
            end = p + M - 1

        elif p > end:
            distance += (p - end)
            end = p
            start = end - M + 1

    return distance

if __name__ == "__main__":
    N, M = map(int, input().split())
    j = int(input())
    print(algorithm())