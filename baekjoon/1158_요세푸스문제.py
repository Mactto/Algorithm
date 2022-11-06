import sys
from collections import deque

def input():
    return sys.stdin.readline()

def solution():
    result = "<"
    N, K = map(int, input().split())
    count = 0
    circle_queue = deque()
    for i in range(N):
        circle_queue.append(i+1)
        
    while circle_queue:
        count += 1
        person = circle_queue.popleft()

        if count % K == 0:
            result += str(person) + ", "
        else:
            circle_queue.append(person)
    
    result = result[0:-2]
    result += ">"
    return result

print(solution())