from collections import deque

N, M = map(int, input().split())

visited = [False for _ in range(100_001)]

def bfs(start):
    queue = deque([[start, 0]])

    while queue:
        num, count = queue.popleft()
        if num == M:
            return count

        if num * 2 <= 100_000 and not visited[num * 2]:
            queue.append([num*2, count])
            visited[num*2] = True
        if num - 1 > -1 and not visited[num - 1]:
            queue.append([num-1, count + 1])
            visited[num-1] = True
        if num + 1 < 100_000 and not visited[num + 1]:
            queue.append([num+1, count + 1])
            visited[num+1] = True

print(bfs(N))