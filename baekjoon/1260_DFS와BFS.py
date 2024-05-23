from collections import deque

N, M, V = map(int, input().split())

connect_dict = {}

for i in range(1, N+1):
    connect_dict[i] = set()

for _ in range(M):
    start_v, end_v = map(int, input().split())
    connect_dict[start_v].add(end_v)
    connect_dict[end_v].add(start_v)

def solution():
    visited = [False for _ in range(N + 1)]

    def dfs(vertex):
        visited[vertex] = True
        print(vertex, end=" ")

        for c in connect_dict[vertex]:
            if visited[c] == False:
                dfs(c)
    
    dfs(V)
    print()


    def bfs(vertex):
        visited = [False for _ in range(N + 1)]
        queue = deque([vertex])

        while queue:
            v = queue.popleft()
            visited[v] = True
            print(v, end=" ")

            for c in connect_dict[v]:
                if visited[c] == False:
                    queue.append(c)
                    visited[c] = True
        

    bfs(V)

solution()