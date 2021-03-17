import sys
input = sys.stdin.readline

def algorithm():
    L.sort()
    result = 0

    for i in range(2, N):
        result = max(result, abs(L[i] - L[i-2]))
    return result

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = list(map(int, input().split()))
        print(algorithm())
