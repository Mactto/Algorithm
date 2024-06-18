from collections import deque

N, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(i, j, visited):
    visited[i][j] = True



def count_ice_mountain():
    count = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                count += 1
                dfs(i, j, visited)



def one_years_later():
    ...


year = 0
while True:
    if count_ice_mountain() > 1:
        print(year)
        break

    one_years_later()