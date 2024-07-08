import heapq

N, M = map(int, input().split())

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

maps = []
for _ in range(M):
    maps.append(list(input()))

def dijkstra():
    pq = []
    cost_table = [[-1 for _ in range(N)] for _ in range(M)]

    heapq.heappush(pq, [0, [0, 0]])

    while pq:
        cost, point = heapq.heappop(pq)
        x = point[0]
        y = point[1]

        if cost_table[x][y] == -1:
            cost_table[x][y] = cost

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < M and 0 <= ny < N:
                    heapq.heappush(pq, [cost + int(maps[nx][ny]), [nx, ny]])

    return cost_table[M-1][N-1]

print(dijkstra())