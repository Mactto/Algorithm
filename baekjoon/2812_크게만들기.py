import sys
input = sys.stdin.readline

def algorithm():
    result, k = [], K
    for i in range(N):
        while k > 0 and result:
            if result[-1] < num[i]:
                result.pop()
                k -= 1
            else:
                break
        result.append(num[i])
    print("".join(result[:N-K]))

if __name__ == "__main__":
    N, K = map(int, input().split())
    num = list(input().rstrip())
    algorithm()

