import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
picture = [list(input().strip()) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]
normal_count, blindness_count = 0, 0


def dfs(point):
    global picture

    x, y = point
    color = picture[x][y]
    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and picture[nx][ny] == color:
            dfs([nx, ny])


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs([i, j])
            normal_count += 1

for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs([i, j])
            blindness_count += 1
print(normal_count, blindness_count)
