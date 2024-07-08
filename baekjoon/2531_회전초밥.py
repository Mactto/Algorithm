from collections import Counter

N, d, k, c = map(int, input().split())

chobaps = []
for _ in range(N):
    chobap = int(input())
    if chobap != c:
        chobaps.append(chobap)


chobaps = chobaps + chobaps

choice = Counter(chobaps[:k])

result = len(choice)
for i in range(k, len(chobaps)):

    choice[chobaps[i-k]] -= 1
    if chobaps[i] in choice:
        choice[chobaps[i]] += 1
    else:
        choice[chobaps[i]] = 1
    result = max(result, len(choice))

print(result + 1)