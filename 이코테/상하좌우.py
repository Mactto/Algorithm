import sys
input = sys.stdin.readline

N = int(input())
words = list(input().split())
direct = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}
x, y = 1, 1

for w in words:
    nx, ny = direct[w]
    if 0 < nx + x <= N and 0 < ny + y <= N:
        x = x + nx
        y = y + ny
print(x, y)