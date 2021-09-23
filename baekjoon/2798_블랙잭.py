import sys
input = sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
cards = list(permutations(cards, 3))

for card in cards:
    total = sum(card)
    if total <= M:
        answer = max(answer, total)
print(answer)