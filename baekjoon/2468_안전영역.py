import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(point, visited):
    y, x = point
    visited.append([x,y])
    print(i, j)

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if loc[nx][ny] > 4 and [nx,ny] not in visited:
                dfs([nx,ny], visited) 

if __name__ == "__main__":
    N = int(input())
    loc = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            if loc[i][j] > 4 and [i,j] not in visited:
                result += 1
                dfs([i,j], visited)
    print(result)