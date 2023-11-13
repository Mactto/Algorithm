import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for to_node, to_cost in graph[now]:
            cost = dist + to_cost

            if cost < distance[to_node]:
                distance[to_node] = cost
                heapq.heappush(q, (cost, to_node))

dijkstra(K)

for d in distance[1:]:
    if d == int(1e9):
        print("INF")
    else:
        print(d)
