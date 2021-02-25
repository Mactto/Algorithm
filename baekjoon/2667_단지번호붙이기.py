import sys
input = sys.stdin.readline


def dfs(point):
    global matrix, count

    x, y = point
    matrix[x][y] = '0'
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] == '1':
                dfs([nx, ny])


if __name__ == "__main__":
    N = int(input())
    matrix = [list(input().rstrip()) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    result = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '1':
                count = 0
                dfs([i, j])
                result.append(count)
    print(len(result))
    for r in result:
        print(r)
