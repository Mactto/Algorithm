n, k = map(int, input().split())

coins = []
case_list = [0 for _ in range(k+1)]
case_list[0] = 1

for _ in range(n):
    coins.append(int(input()))

for value in range(1, k+1):
    for coin in coins:
        print(value, coin, value-coin)
        if value - coin >= 0:
            case_list[value] += max(case_list[value - coin], case_list[value])

print(case_list)