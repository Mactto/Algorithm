import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [(0, 0)] * (N + 1)

    dp[0] = (1, 0)
    if N == 0:
        result_zero, result_one = dp[0]
        print(result_zero, result_one)
        continue

    dp[1] = (0, 1)
    if N == 1:
        result_zero, result_one = dp[1]
        print(result_zero, result_one)
        continue

    for i in range(2, N+1):
        zero_1, one_1 = dp[i-1]
        zero_2, one_2 = dp[i-2]
        dp[i] = (zero_1 + zero_2, one_1 + one_2)

    result_zero, result_one = dp[N]
    print(result_zero, result_one)
    


