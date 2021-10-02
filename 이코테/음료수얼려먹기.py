import sys
input = sys.stdin.readline

N, M = map(int, input().split())
frame = [list(map(int, input().strip())) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
count = 0

def dfs(x, y):
    frame[x][y] = 1

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0 <= nx < N and 0 <= ny < M:
            if frame[nx][ny] == 0:
                dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if frame[i][j] == 0:
            count += 1
            dfs(i, j)
print(count)