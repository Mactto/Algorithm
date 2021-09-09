import sys
input = sys.stdin.readline

N = int(input())
l = []
for i in range(N):
    num = int(input())
    l.append(num)
    l.sort()
    if len(l) % 2 == 0:
        print(l[len(l)//2-1])
    else:
        print(l[len(l)])