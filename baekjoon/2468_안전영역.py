import sys
input = sys.stdin.readline

def dfs(point, visited, k):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        x, y = point
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and loc[nx][ny] > k and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs([nx, ny], visited, k)

if __name__ == "__main__":
    N = int(input())
    loc = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for k in range(max(map(max, loc))):
        visited = [[0] * N for _ in range(N)]
        count = 0

        for i in range(N):
            for j in range(N):
                if loc[i][j] > k and visited[i][j] != 1:
                    count += 1
                    visited[i][j] = 1
                    dfs([i, j], visited, k)
        answer = max(count, answer)
    print(answer)
