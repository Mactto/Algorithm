import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

dp = [[INF] * N for _ in range(N)]
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]


for i in range(N-1):
    for j in range(N):
        if j == 0:
            dp[i+1][j+1] = min(dp[i][j] + costs[i+1][j+1], dp[i+1][j+1])
            dp[i+1][j+2] = min(dp[i][j] + costs[i+1][j+2], dp[i+1][j+2])
        elif j == 1:
            dp[i+1][j-1] = min(dp[i][j] + costs[i+1][j-1], dp[i+1][j-1])
            dp[i+1][j+1] = min(dp[i][j] + costs[i+1][j+1], dp[i+1][j+1])
        elif j == 2:
            dp[i+1][j-1] = min(dp[i][j] + costs[i+1][j-1], dp[i+1][j-1])
            dp[i+1][j-2] = min(dp[i][j] + costs[i+1][j-2], dp[i+1][j-2])

print(min(dp[-1]))