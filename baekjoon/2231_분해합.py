import sys
input = sys.stdin.readline

N = int(input())
flag = False
answer = 0

for i in range(N):
    values = list(map(int, str(i)))
    if i + sum(values) == N:
        answer = i
        flag = True
        break

if flag:
    print(answer)
else:
    print(0)