# cost = list(map(int, input().split()))
# cost.append(0)
# stair_cost = [0 for _ in range(len(cost) + 1)]

# def dp(n):
#     if n == 0:
#         return cost[0]
#     if n == 1:
#         return cost[1]

#     if stair_cost[n] != 0:
#         return stair_cost[n]
#     else:
#         return cost[n] + min(dp(n-1), dp(n-2))
    
# print(dp(len(cost)-1))

cost = list(map(int, input().split()))
stair_cost = [0 for _ in range(len(cost) + 1)]

def dp(n):
    stair_cost[0] = cost[0]
    stair_cost[1] = cost[1]

    for i in range(2, n):
        stair_cost[i] = cost[i] + min(stair_cost[i-1], stair_cost[i-2])

    return min(stair_cost[n-1], stair_cost[n-2])
    
print(dp(len(cost)))