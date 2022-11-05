import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def push(queue, x):
    queue.append(x)

def pop(queue):
    if empty(queue):
        return -1
    return queue.popleft()

def size(queue):
    return len(queue)

def empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0

def front(queue):
    if empty(queue):
        return -1
    return queue[0]

def back(queue):
    if empty(queue):
        return -1
    return queue[-1]

def solution():
    queue = deque()
    n = int(input())

    for _ in range(n):
        operate = input()
        operate = operate.split(' ')

        if operate[0] == "push":
            push(queue, operate[1])
        elif operate[0] == "pop":
            print(pop(queue))
        elif operate[0] == "size":
            print(size(queue))
        elif operate[0] == "empty":
            print(empty(queue))
        elif operate[0] == "front":
            print(front(queue))
        elif operate[0] == "back":
            print(back(queue))



solution()