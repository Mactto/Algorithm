from collections import deque

def solution(rooms):
    edge_dict = {}
    visited = [False for _ in range(len(rooms))]

    for idx, r in enumerate(rooms):
        edge_dict[idx] = r
        
    def dfs(vertex):
        visited[vertex] = True

        for k in edge_dict[vertex]:
            if visited[k] == False:
                dfs(k)

    def bfs(vertex):
        queue = deque([vertex])

        while queue:
            vertex = queue.popleft()
            visited[vertex] = True

            for k in edge_dict[vertex]:
                if visited[k] == False:
                    queue.append(k)

    dfs(0)
    # bfs(0)

    if False in visited:
        return 'X'
    else:
        return 'O'


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(solution(rooms))