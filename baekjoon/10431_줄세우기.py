T = int(input())

for _ in range(T):
    user_input = list(map(int, input().split()))
    talls = user_input[1:]

    count = 0

    for i in range(len(talls) -1, -1, -1):
        for j in range(i):
            if talls[j] > talls[j+1]:
                talls[j], talls[j+1] = talls[j+1], talls[j]
                count += 1

    print(user_input[i], count)
