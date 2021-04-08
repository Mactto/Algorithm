import sys
input = sys.stdin.readline

def algorithm():
    diff = []

    for i in range(N-1):
        diff.append(height[i+1] - height[i])
    diff.sort()

    answer = 0
    for i in range(N-K):
        answer += diff[i]
    return answer
        

        

if __name__ == "__main__":
    N, K = map(int, input().split())
    height = [list(map(int, input().split()))]
    print(algorithm())