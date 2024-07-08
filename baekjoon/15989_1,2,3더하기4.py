T = int(input())

for _ in range(T):
    num = int(input())

    count = 1

    count += num // 2
    count += num // 3

    for v in range(3, num, 3):
        count += (num - v) // 2

    print(count)