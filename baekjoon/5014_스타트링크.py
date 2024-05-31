from collections import deque


F, S, G, U, D = map(int, input().split())


def bfs():
    queue = deque([])
    queue.append([S, 0])
    visited = [False for _ in range(F + 1)]
    visited[S] = True

    while queue:
        floor, count = queue.popleft()
        if floor == G:
            return count
        if floor + U <= F and not visited[floor + U]:
            queue.append([floor + U, count + 1])
            visited[floor + U] = True
        if floor - D > 0 and not visited[floor - D]:
            queue.append([floor - D, count + 1])
            visited[floor - D] = True

    return "use the stairs"

print(bfs())