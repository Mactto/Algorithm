import sys
import heapq
input = sys.stdin.readline

# 데드라인 기준이 아닌 컵라면 개수를 기준으로 잡는다는 것이 핵심

def algorithm(info):
    heap = []

    for i in info:
        heapq.heappush(heap, i[1])
        if i[0] < len(heap):
            heapq.heappop(heap)
    return sum(heap)

if __name__ == "__main__":
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    info.sort()
    print(algorithm(info))