import sys

def push(stack, x):
    stack.append(x)

def pop(stack):
    if empty(stack):
        return -1
    return stack.pop(-1)

def size(stack):
    return len(stack)

def empty(stack):
    if len(stack) == 0:
        return 1
    else:
        return 0

def top(stack):
    if empty(stack):
        return -1
    return stack[-1]

def solution():
    n = int(sys.stdin.readline().rstrip())
    stack = []

    for _ in range(n):
        operate = sys.stdin.readline().rstrip()
        operate = operate.split(' ')
        if operate[0] == "push":
            push(stack, operate[1])
        elif operate[0] == "pop":
            print(pop(stack))
        elif operate[0] == "size":
            print(size(stack))
        elif operate[0] == "top":
            print(top(stack))
        elif operate[0] == "empty":
            print(empty(stack))


solution()