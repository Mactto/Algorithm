import sys
input = sys.stdin.readline

def algorithm():
    diff = []

    for i in range(1, N):
        diff.append(height[i] - height[i-1])
    diff.sort()

    answer = 0
    for i in range(N-K):
        print(diff[i])
        answer += diff[i]
    return answer
        
if __name__ == "__main__":
    N, K = map(int, input().split())
    height = list(map(int, input().split()))
    print(algorithm())