import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
n = 1
result = 0

while(n <= M):
    if n % K == 0:
        result += numbers[1]
    else:
        result += numbers[0]
    n += 1
print(result)