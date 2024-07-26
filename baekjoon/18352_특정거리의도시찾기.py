import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph: dict[list] = {}
for i in range(1, N+1):
    graph[i] = []

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)


def dijkstra(start):
    pq = []
    cost = {}

    heapq.heappush(pq, [0, start])

    while pq:
        c, n = heapq.heappop(pq)

        if n not in cost:
            cost[n] = c

            for next_node in graph[n]:
                heapq.heappush(pq, [c+1, next_node])
    
    return cost

result = dijkstra(X)
count = 0
for key, value in result.items():
    if value == K:
        print(key)
        count += 1

if count == 0:
    print(-1)


