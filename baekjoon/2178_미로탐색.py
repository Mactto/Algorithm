from collections import deque

N, M = map(int, input().split())

miro = []
for _ in range(N):
    miro.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0 for _ in range(M)] for _ in range(N)]


def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    visited[0][0] = 1

    while queue:
        x, y, count = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append([nx, ny, count + 1])
                visited[nx][ny] = count + 1

    return visited[N-1][M-1]


print(bfs())