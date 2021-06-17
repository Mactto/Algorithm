import sys
input = sys.stdin.readline

def algorithm(L):
    for i in range(N):
        if L < height[i]:
            return L
        L += 1
    return L

if __name__ == "__main__":
    N, L = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort()
    print(algorithm(L))