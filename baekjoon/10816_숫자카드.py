import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

cards_dict = {}
for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

for number in numbers:
    if number in cards_dict:
        print(cards_dict[number], end=' ')
    else:
        print(0, end=' ')