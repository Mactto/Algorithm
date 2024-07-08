N, K, P, X = map(int, input().split())

LED_LIGNHT = {
    0: [1,1,1,0,1,1,1],
    1: [0,0,1,0,0,1,0],
    2: [1,0,1,1,1,0,1],
    3: [1,0,1,1,0,1,1],
    4: [0,1,1,1,0,1,0],
    5: [1,1,0,1,0,1,1],
    6: [1,1,0,1,1,1,1],
    7: [1,1,1,0,0,1,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1]
}

result = 0
bitmap = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i == j: continue
        
        diff = 0
        for n1, n2 in zip(LED_LIGNHT[i], LED_LIGNHT[j]):
            if n1 != n2:
                diff += 1
        
        bitmap[i][j] = diff
        bitmap[j][i] = diff

N = str(N)
X = str(X)
if len(N) < len(X):
    N = "0" * (len(X) - len(N)) + N
elif len(N) > len(X):
    X = "0" * (len(N) - len(X)) + X

tempX = int(X)
for i in range(10 ** (K-1), int(N)+1):
    if tempX == i: continue

    X = list(X)
    target = list(str(i))

    count = 0
    for x, t in zip(X, target):
        count += bitmap[int(x)][int(t)]
        if count > P:
            break
    
    if count <= P:
        result += 1

print(result)
