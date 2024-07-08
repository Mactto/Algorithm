N, M = map(int, input().split())

space = []
for _ in range(N):
    space.append(list(map(int, input().split())))
result = []

def dfs(i: int, j: int, d: int, r: int):
    nr = space[i][j] + r

    if i + 1 >= N:
        result.append(nr)
        return
    
    for k in [-1, 0, 1]:
        if d != k and 0 <= j + k < M:
            dfs(i+1, j+k, k, nr)

for x in range(M):
    dfs(0, x, 2, 0)

print(min(result))