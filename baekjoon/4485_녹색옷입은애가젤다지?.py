import heapq

dx = [0,0,-1,1]
dy = [-1,1,0,0]

problem = 1
while True:
    N = int(input())

    if N == 0:
        break

    maps = []
    pq = []
    visited = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(N):
        maps.append(list(map(int, input().split())))

    heapq.heappush(pq, [maps[0][0], 0, 0])

    while pq:
        c, x, y = heapq.heappop(pq)

        if not visited[x][y]:
            maps[x][y] = c
            visited[x][y] = True

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    heapq.heappush(pq, [c + maps[nx][ny], nx, ny])


    print(f"Problem {problem}: {maps[N-1][N-1]}")
    problem += 1

