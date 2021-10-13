import sys
input = sys.stdin.readline

N = int(input())
res = list(map(int, input().split()))
M = int(input())
req = list(map(int, input().split()))

def binary_search(array, target , start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

res.sort()
flag = True
for r in req:
    flag = binary_search(res, r, 0, N-1)
    if flag:
        print('yes', end=' ')
    else:
        print('no', end=' ')
