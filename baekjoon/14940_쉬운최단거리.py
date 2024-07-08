from collections import deque

N, M = map(int, input().split())

maps = []
result = [[-1 for _ in range(M)] for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
for _ in range(N):
    maps.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            queue.append([i, j])
            result[i][j] = 0
            start_x = i
            start_y = j
        elif maps[i][j] == 0:
            result[i][j] = 0

while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < M and result[nx][ny] == -1 and maps[nx][ny] != 0:
            result[nx][ny] = result[x][y] + 1
            queue.append([nx, ny])

result[start_x][start_y] = 0

for r in result:
    print(' '.join(map(str, r)))