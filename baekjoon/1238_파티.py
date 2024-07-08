import heapq

N, M, X = map(int, input().split())

graph = {}

for i in range(N):
    graph[i+1] = []

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])


def dijstra(start):
    pq = []
    cost = {}

    heapq.heappush(pq, [0, start])

    while pq:
        c, n = heapq.heappop(pq)

        if n not in cost:
            cost[n] = c

            for next_n, next_c in graph[n]:
                heapq.heappush(pq, [c + next_c, next_n])
    
    return cost

cost = dijstra(X)

for i in range(1, N+1):
    if i == X:
        continue
    go_cost = dijstra(i)
    cost[i] += go_cost[X]

print(max(cost.values()))