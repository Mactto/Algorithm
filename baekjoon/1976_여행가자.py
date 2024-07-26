N = int(input())
M = int(input())

visited = [False for _ in range(N + 1)]
graph = {}
for i in range(1, N+1):
    graph[i] = set()

for i in range(1, N + 1):
    road = list(map(int, input().split()))

    for idx, value in enumerate(road):
        if value == 1:
            graph[idx+1].add(i)
            graph[i].add(idx+1)

path = list(map(int, input().split()))

from collections import deque

def bfs(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited[node] = True

        for next in graph[node]:
            if not visited[next]:
                queue.append(next)

bfs(path[0])

result = "YES"
for p in set(path):
    if visited[p] == False:
        result = "NO"

print(result)