import sys
input = sys.stdin.readline

def algorithm():
    dist = []
    result = 0
    for i in range(len(point)-1):
        dist.append(point[i+1] - point[i])
    dist.sort(reverse=True)
    
    for _ in range(K -1):
        dist.pop(0)
    return sum(dist)

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    point = list(map(int, input().split()))
    point.sort()
    if K >= N:
        print(0)
    else:
        print(algorithm())
