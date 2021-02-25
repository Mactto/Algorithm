import sys
input = sys.stdin.readline


def dfs(com):
    global count, visited
    count += 1
    visited[com] = True

    for i in range(1, N+1):
        if not visited[i] and matrix[com][i] == 1:
            dfs(i)


if __name__ == "__main__":
    N = int(input())
    E = int(input())
    matrix = [[0] * (N+1) for _ in range(N+1)]
    visited = [False] * (N+1)
    count = -1
    for _ in range(E):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        matrix[y][x] = 1
    dfs(1)
    print(count)
