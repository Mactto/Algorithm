import sys
input = sys.stdin.readline

N = int(input())
have_number_card = list(map(int, input().split()))
M = int(input())
number_card = list(map(int, input().split()))

number_card_dict = {}
for hnc in have_number_card:
    number_card_dict[hnc] = 1

for nc in number_card:
    if nc in number_card_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')