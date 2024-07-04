N, M = map(int, input().split())

alias_list = []
stat_list = []
for _ in range(N):
    alias, stat = map(str, input().split())
    stat_list.append(int(stat))
    alias_list.append(alias)

def binary_search(p):
    left = 0
    right = len(stat_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if p <= stat_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return right + 1

for _ in range(M):
    s = int(input())
    idx = binary_search(s)
    print(alias_list[idx])