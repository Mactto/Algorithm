import sys
import heapq
input = sys.stdin.readline


def algorithm(info):
    heap = []

    for i in info:
        heapq.heappush(heap, i[1])
        print("heap push : ", heap)
        if i[0] < len(heap):
            heapq.heappop(heap)
            print("heap pop : ", heap)
    return sum(heap)

if __name__ == "__main__":
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    info.sort()
    print(info)
    print(algorithm(info))