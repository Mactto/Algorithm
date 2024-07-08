N = int(input())
target = list(input())

result = 0
for _ in range(N-1):
    word = list(input())
    target_copy = target[:]
    count = 0

    for w in word:
        if w in target_copy:
            target_copy.remove(w)
        else:
            count += 1
        
    if count < 2 and len(target_copy) < 2:
        result += 1

print(result)
