import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

result = 0
for c in cards:
    result = max(result, min(c))
print(result)