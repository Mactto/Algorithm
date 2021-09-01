import sys
input = sys.stdin.readline

N = int(input())
aparts = [list(input().strip()) for _ in range(N)]
count = 0
apart_nums = 0
result = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(point):
    global aparts, apart_nums
    x, y = point
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N and aparts[ny][nx] == '1':
            apart_nums += 1
            aparts[ny][nx] = '2'
            dfs([nx, ny])


for i in range(N):
    for j in range(N):
        if aparts[i][j] == '1':
            apart_nums = 0
            count += 1
            dfs([j, i])
            if count > 0 and apart_nums == 0:
                apart_nums += 1
            result.append(apart_nums)
print(count)
result.sort()
for r in result:
    print(r)
