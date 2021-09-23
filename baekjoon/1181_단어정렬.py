import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
result = []
words = set(words)
for w in words:
    result.append([w, len(w)])
result = sorted(result, key=lambda x: x[0])
result = sorted(result, key=lambda x: x[1])

for r in result:
    print(r[0])
