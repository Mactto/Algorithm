import sys
input = sys.stdin.readline

def bfs():
    queue = [[0,0]]
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    while queue:
        x, y = queue.pop(0)

        if x == N-1 and y == M-1:
            return(visited[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and miro[nx][ny] == '1':
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


if __name__ == "__main__":
    N, M = map(int, input().split())
    miro = [input().rstrip() for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print(bfs())