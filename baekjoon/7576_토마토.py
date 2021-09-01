from collections import deque
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append([j, i])

    def bfs():
        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
                    queue.append([nx, ny])
                    box[ny][nx] = box[y][x] + 1
    bfs()
    flag = False
    result = -2

    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                flag = True
            result = max(result, box[i][j])
    if flag:
        print(-1)
    elif result == -1:
        print(0)
    else:
        print(result-1)
