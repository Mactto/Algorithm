import sys
input = sys.stdin.readline

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    print(factorial(M) // (factorial(N) * factorial(M - N)))