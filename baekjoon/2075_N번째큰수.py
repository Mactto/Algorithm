N = int(input())

result = []
for _ in range(N):
    result.extend(list(map(int, input().split())))
    result.sort()
    result = result[-N:]

print(result[0])    
