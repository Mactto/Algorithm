import sys
from collections import deque

def input():
    return sys.stdin.readline()

def solution():
    N = int(input())
    cards = deque([i+1 for i in range(N)])

    if len(cards) == 1:
        return cards[0]
    
    while cards:
        if len(cards) == 2:
            return cards[-1]
        cards.popleft()
        cards.append(cards.popleft())
    

print(solution())