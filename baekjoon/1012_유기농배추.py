import sys
input = sys.stdin.readline

def dfs(point):
    global farm
    y, x = point
    farm[x][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if farm[ny][nx] == 1:
                dfs([ny, nx])

if __name__ == "__main__": 
    T = int(input())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    for _ in range(T):
        M, N, K = map(int, input().split())
        farm = [[0] * M for _ in range(N)]
        for _ in range(K):
            a, b = map(int, input().split())
            farm[b][a] = 1
        for a in range(M):
            for b in range(N):
                if farm[a][b] == 1:
                    result += 1
                    dfs([a, b])
        print(result)