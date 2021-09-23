import sys
input = sys.stdin.readline

N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]
point = sorted(point, key=lambda x: x[1])
point = sorted(point, key=lambda x: x[0])
for x, y in point:
    print(x, y)
