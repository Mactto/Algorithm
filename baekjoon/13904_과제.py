import sys
import heapq
input = sys.stdin.readline

def algorithm(heap):
    score = [0] * (1000+1)
    while heap:
        temp = heapq.heappop(heap)
        for i in range(temp[1], 0, -1):
            if (score[i] == 0):
                score[i] = temp[2]
                break
    return sum(score)


if __name__ == "__main__":
    N = int(input())
    heap = []
    for _ in range(N):
        d, w = map(int, input().split())
        heapq.heappush(heap, [-w, d, w])
    print(algorithm(heap))