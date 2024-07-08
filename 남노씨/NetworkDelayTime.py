import heapq

times = [[2,1,2], [2,3,5], [2,4,1], [4,3,3]]
n = 4
k = 3

graph = {}
visited = [0 for _ in range(n)]
for i in range(n):
    graph[i+1] = []

for s, e, c in times:
    graph[s].append([c, e])

def dijkstra(start):
    pq = []

    heapq.heappush(pq, [0, start])

    while pq:
        c, n = heapq.heappop(pq)
        if n-1 not in visited:
            visited[n-1] = 1
            for nc, nn in graph[n]:
                heapq.heappush(pq, [c + nc, nn])

        if sum(visited) == n:
            return c
    return -1

print(dijkstra(k))