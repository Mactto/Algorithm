import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [x for x in range(1, N+1)]

lists = combinations(numbers, M)
for list in lists:
    for l in list:
        print(l, end=' ')
    print()
