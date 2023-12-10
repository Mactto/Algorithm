import sys
input = sys.stdin.readline

n = int(input())
integers = list(map(int, input().split()))

for i in range(1, n):
    integers[i] = max(integers[i-1] + integers[i], integers[i])
print(integers)
print(max(integers))