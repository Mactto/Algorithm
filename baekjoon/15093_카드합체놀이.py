import sys
import heapq
input = sys.stdin.readline

def algorithm():
    for _ in range(M):
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        s_num = n1 + n2
        heapq.heappush(heap, s_num)
        heapq.heappush(heap, s_num)
    return sum(heap)


if __name__ == "__main__":
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    heap = []
    for i in range(N):
        heapq.heappush(heap, a[i])
    print(algorithm())
