import sys
import heapq
input = sys.stdin.readline

def algorithm():
    result = 0
    heapq.heapify(heap)

    if len(heap) == 1:
        return 0
    else:
        while len(heap) > 1:
            value = heapq.heappop(heap) + heapq.heappop(heap)
            result += value
            heapq.heappush(heap, value)
    
    return result

if __name__ == "__main__":
    N = int(input())
    heap = [int(input()) for _ in range(N)]
    print(algorithm())
