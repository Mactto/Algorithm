import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [x for x in range(1, N+1)]

lists = permutations(numbers, M)
for list in lists:
    for l in list:
        print(l, end=' ')
    print()
