import sys
input = sys.stdin.readline

N = int(input())
grades = [list(input().strip().split()) for _ in range(N)]

grades = sorted(grades, key=lambda x: int(x[1]))
for g in grades:
    print(g[0], end=' ')