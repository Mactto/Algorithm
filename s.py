import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] * 10001

for _ in range(N):
    n = int(input())
    numbers[n] += 1

for i in range(10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)
