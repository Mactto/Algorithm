import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort(reverse=True)
for n in numbers:
    print(n, end=' ')