from collections import deque

dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
boxes = []

for _ in range(H):
    box_row = []
    for _ in range(N):
        box_row.append(list(map(int, input().split())))
    boxes.append(box_row)

def bfs():
    queue = deque()

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[h][i][j] == 1:
                    visited[h][i][j] = 1
                    queue.append([h, i, j, 0])

    while queue:
        z, y, x, d = queue.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and visited[nz][ny][nx] == 0 and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                visited[nz][ny][nx] = d + 1
                queue.append([nz, ny, nx, d + 1])

    max_day = 0

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[h][i][j] == 0:
                    return -1
                max_day = max(max_day, visited[h][i][j])

    return max_day


flag = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[h][i][j] == 0:
                flag = True
                
if not flag:
    print(0)
else:
    print(bfs())