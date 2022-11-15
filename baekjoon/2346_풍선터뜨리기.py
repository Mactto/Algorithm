import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    result = ""
    N = int(input())
    ballon_list = list(map(int, input().split()))
    queue = deque([i+1, ballon_list[i]] for i in range(N))
    while queue:
        idx, rot = queue.popleft()
        result += str(idx) + " "
        if rot > 0:
            queue.rotate(-rot+1)
        else:
            queue.rotate(-rot)

    return result[:-1]

print(solution())

