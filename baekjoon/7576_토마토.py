import sys
input = sys.stdin.readline


def bfs():
    global queue, day

    while queue:
        day += 1
        for q in queue:
            x, y = q
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M:
                    if box[nx][ny] == 0:
                        box[nx][ny] = 1
                        queue.append([nx, ny])


if __name__ == "__main__":
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    queue = []
    day = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append([i, j])
    bfs()
    print(day)
