import sys
input = sys.stdin.readline

board = [[0] * 100 for _ in range(100)]

n = int(input())

point = []
for _ in range(n):
    point.append(map(int, input().split()))

for x, y in point:
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1


answer = 0
for b in board:
    answer += b.count(1)

print(answer)