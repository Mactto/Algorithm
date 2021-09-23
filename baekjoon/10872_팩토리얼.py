import sys
input = sys.stdin.readline

N = int(input())

def dfs(n):
    result = 1
    if n > 0:
        result = n * dfs(n-1)
    print(n, result)
    return result

print(dfs(N))