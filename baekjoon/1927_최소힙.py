import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    x = [int(input()) for _ in range(N)]
    heap = []
    for i in range(N):
        if x[i] > 0:
            heapq.heappush(heap, x[i])

        elif len(heap) == 0:
            print(0)
        elif x[i] == 0:
            print(heapq.heappop(heap))