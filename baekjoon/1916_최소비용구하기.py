import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    G, A, C = map(int, input().split())
    graph[G].append((A, C))

start, end = map(int, input().split())

def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
    
        for go_node, go_cost in graph[now]:
            cost = dist + go_cost

            if cost < distance[go_node]:
                distance[go_node] = cost
                heapq.heappush(q, (cost, go_node))

    return distance[e]

print(dijkstra(start, end))
