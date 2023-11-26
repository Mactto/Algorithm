n = int(input())

def factorial(n):
    memo = [0] * (n + 1)

    for i in range(1, n+1):
        if i == 1:
            memo[i] = 1
        elif i == 2:
            memo[i] = 2
        else:
            memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

print(factorial(n) % 10007)