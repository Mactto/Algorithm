import sys
import heapq
input = sys.stdin.readline

def algorithm(session):
    heap = []

    for s in session:
        heapq.heappush(heap, s[0])
        if s[1] < len(heap):
            heapq.heappop(heap)
    return sum(heap)


if __name__ == "__main__":
    N = int(input())
    session = [list(map(int, input().split())) for _ in range(N)]
    session = sorted(session, key=lambda x: x[1])
    print(algorithm(session))