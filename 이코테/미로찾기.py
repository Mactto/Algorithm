import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque()

def bfs():
    queue.append([0, 0, 1])

    while queue:
        x, y, count = queue.popleft()
        print(x, y)
        visited[x][y] = True
        if x == N-1 and y == M-1:
            return count

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and miro[nx][ny] == 1:
                    queue.append([nx, ny, count+1])

    return False

print(bfs())