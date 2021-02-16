import sys
input = sys.stdin.readline

def algorithm():
    if N > 2:       # N이 2보다 큰 경우
        if M <= 6:
            return min(4, M)
        else:
            return M - 2
    elif N == 2:    # N이 2인 경우
        return min(4, (M+1) // 2)
    else:           # N이 1인 경우
        return 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    print(algorithm())