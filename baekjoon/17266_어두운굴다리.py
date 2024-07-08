N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

lamps.sort()
result = []

result.append(lamps[0] - 0)
result.append(N - lamps[-1])

for i in range(M-1):
    distance = lamps[i+1] - lamps[i]

    if distance % 2 == 0:
        result.append(distance // 2)
    else:
        result.append((distance // 2) + 1)

print(max(result))