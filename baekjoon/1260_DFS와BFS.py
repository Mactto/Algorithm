import sys
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in range(1, N+1):
        if not visited[i] and matrix[start][i] == 1:
            dfs(i)

def bfs(start):
    queue = [start]
    visited = [False] * (N+1)
    visited[start] = True
    print(visited)

    while queue:
        num = queue.pop(0)
        print(num, end=' ')
        for i in range(1, N+1):
            if not visited[i] and matrix[num][i] == 1:
                queue.append(i)
                visited[i] = True

if __name__ == "__main__":
    N, M, V = map(int, input().split())
    matrix = [[0] * (N+1) for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        n1, n2 = map(int, input().split())
        matrix[n1][n2] = 1
        matrix[n2][n1] = 1
        
    dfs(V)
    print()
    bfs(V)


'''
1ㅡ2
ㅣ\ㅣ
3ㅡ4
'''