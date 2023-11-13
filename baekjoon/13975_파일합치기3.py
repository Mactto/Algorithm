import sys
import heapq
input = sys.stdin.readline

T = int(input())
a = []

def solution(pages: list):
    heapq.heapify(pages)
    result = 0
    while len(pages) > 1:
        merge_cost = heapq.heappop(pages) + heapq.heappop(pages)
        result += merge_cost
        heapq.heappush(pages, merge_cost)

    return result

for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    a.append(solution(K, pages))

for aa in a:
    print(aa)
