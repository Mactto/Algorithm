N = int(input())
switchs = [-1] + list(map(int, input().split()))

K = int(input())

def switch(value: int):
    if value == 0:
        return 1
    elif value == 1:
        return 0

def man(num: int):
    n = 1

    while num * n < N:
        switchs[num * n] = switch(switchs[num * n])
        n += 1

def woman(num: int):
    switchs[num] = switch(switchs[num])

    n = 1

    while True:
        if num - n < 1 or num + n > N:
            break

        if switchs[num-n] != switchs[num+n]:
            break
    
        switchs[num-n] = switch(switchs[num-n])
        switchs[num+n] = switch(switchs[num+n])
        n += 1

for _ in range(K):
    s, v = map(int, input().split())

    if s == 1:
        man(v)
    elif s == 2:
        woman(v)

for i in range(1, N+1):
    print(switchs[i], end=' ')