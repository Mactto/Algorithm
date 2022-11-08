import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

queue = deque()

def push_front(x):
    queue.appendleft(x)

def push_back(x):
    queue.append(x)

def pop_front():
    if empty(): return -1
    return queue.popleft()

def pop_back():
    if empty(): return -1
    return queue.pop()

def size():
    return len(queue)

def empty():
    if len(queue) == 0:
        return 1
    else:
        return 0

def front():
    if empty(): return -1
    return queue[0]

def back():
    if empty(): return -1
    return queue[-1]

def solution():
    N = int(input())

    for _ in range(N):
        operate = input()
        operate = operate.split(" ")
        
        if operate[0] == "push_front":
            push_front(operate[1])
        elif operate[0] == "push_back":
            push_back(operate[1])
        elif operate[0] == "front":
            print(front())
        elif operate[0] == "back":
            print(back())
        elif operate[0] == "size":
            print(size())
        elif operate[0] == "empty":
            print(empty())
        elif operate[0] == "pop_front":
            print(pop_front())
        elif operate[0] == "pop_back":
            print(pop_back())

solution()