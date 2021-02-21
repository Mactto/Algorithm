import heapq
import sys
input = sys.stdin.readline

def algorithm():
    result = 0
    en = []

    for _ in range(K):
        bag = heapq.heappop(C)

        while info and bag >= info[0][0]:
            weight, value = heapq.heappop(info)
            heapq.heappush(en, -value)
        if en:
            result -= heapq.heappop(en)
        elif not info:
            break
    return result

if __name__ == "__main__":
    N, K = map(int, input().split())
    info = []
    C = []
    for _ in range(N):
        heapq.heappush(info, list(map(int, input().split())))
    for _ in range(K):
        heapq.heappush(C, int(input()))
    print(algorithm())