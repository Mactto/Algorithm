import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (N + 1)
    
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
    
        for go_node, go_cost in graph[now]:
            cost = dist + go_cost

            if distance[go_node] > cost:
                distance[go_node] = cost
                heapq.heappush(q, (cost, go_node))

    return distance[end]

result = min(
    dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
    dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N),
)

print(result if result < INF else -1)