from collections import deque

def solution(land):
    result = [0 for _ in range(len(land[0]))]
    visited = [[ False for _ in range(len(land[0]))] for _ in range(len(land))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    def bfs(x, y):
        count = 0
        column_set = set()
        queue = deque([[x, y]])
        visited[x][y] = True
        
        while queue:
            i, j = queue.popleft()
            column_set.add(j)
            count += 1
        
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

        for cs in column_set:
            result[cs] += count

    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j] == 1:
                bfs(i, j)
    

    return max(result)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]	))