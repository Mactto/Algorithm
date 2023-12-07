import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = {}
visited = [0] * (N + 1)
result = [0] * (N + 1)

for i in range(1, N + 1):
    graph[i] = []

for _ in range(1, N):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)



queue = deque([1])
while queue:
    node = queue.popleft()
    visited[node] = 1

    for child in graph[node]:
        if not visited[child]:
            result[child] = node
            queue.append(child)

for r in result[2:]:
    print(r)