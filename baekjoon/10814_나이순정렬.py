import sys
input = sys.stdin.readline

N = int(input())
users = [input().strip().split() for _ in range(N)]
users = sorted(users, key=lambda x: int(x[0]))

for age, name in users:
    print(age, name)
