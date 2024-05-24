from collections import deque

N = int(input())

maps = []
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    maps.append(list(map(int, input())))


def bfs(x, y):
    count = 1
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True
                count += 1

    return count

result = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            result.append(bfs(i, j))

result.sort()
print(len(result))
for r in result:
    print(r)