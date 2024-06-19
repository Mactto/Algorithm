N = int(input())
pan = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(i: int, j: int, direct: tuple):
    visited[i][j] = True
    count = 1

    while True:
        dx, dy = direct
        nx = i + dx
        ny = j + dy

        if not 0 <= nx < N or not 0 <= ny < N or visited[nx][ny] or pan[nx][ny] != '*':
            break

        count += 1
        i = nx
        j = ny

    return count

def solution():
    for i in range(N):
        for j in range(N):
            if pan[i][j] == '*':
                visited[i][j] = True
                visited[i+1][j] = True
                left_arm = dfs(i+1, j-1, (0, -1))
                right_arm = dfs(i+1, j+1, (0, 1))
                waist = dfs(i+2, j, (1, 0))
                left_leg = dfs(i + waist + 2, j-1, (1, 0))
                right_leg = dfs(i + waist + 2, j+1, (1, 0))
                print(i+2, j+1)
                print(left_arm, right_arm, waist, left_leg, right_leg)
                return
            
solution()