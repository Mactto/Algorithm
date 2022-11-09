import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    ascii_value = {}
    stack = deque()
    N = int(input())
    operate = input()
    operate = list(operate)
    result = 0

    for i in range(N):
        n = int(input())
        ascii_value[chr(i+65)] = n
        
    for oper in operate:
        if 64 < ord(oper) and ord(oper) < 91:
            stack.append(ascii_value[oper])
        else:
            oper1 = stack.pop()
            oper2 = stack.pop()
            result = eval(str(oper2) + oper + str(oper1))
            stack.append(result)
        
    return '{:.2f}'.format(round(result, 2))


print(solution())