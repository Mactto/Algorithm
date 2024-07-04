T = int(input())

for _ in range(T):
    N = int(input())
    price_list = list(map(int, input().split()))

    max_income = 0
    max_price = price_list[-1]
    for i in range(N-2, -1, -1):
        if price_list[i] >= max_price:
            max_price = price_list[i]
        else:
            max_income = max_income + (max_price - price_list[i])

    print(max_income)
