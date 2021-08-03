def solution(price, money, count):
    total = 0

    for i in range(1, count+1):
        total += price * i

    if total <= money:
        return 0
    else:
        return total - money


if __name__ == "__main__":
    price = int(input())
    money = int(input())
    count = int(input())
    solution(price, money, count)
