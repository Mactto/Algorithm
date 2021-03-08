import sys
input = sys.stdin.readline

def bfs(v):
    queue = [v]

    while queue:
        v= queue.pop(0)
        for i in range(1, N+1):
            if edge[i][v] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    edge = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        edge[u][v] = 1
        edge[v][u] = 1
    visited = [0] * (N+1)
    count = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            bfs(i)
            count += 1
    print(count)