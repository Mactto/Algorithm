import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    testcase = int(input())

    for _ in range(testcase):
        N, M = map(int, input().split())
        documents = list(map(int, input().split()))
        count = 0
        queue = deque(documents)
        while queue:
            most_important = max(queue)
            first_important = queue.popleft()
            if first_important < most_important:
                queue.append(first_important)
                if M == 0:
                    M = len(queue)
                M -= 1

            if first_important == most_important:
                count += 1
                if M == 0:
                    print(count)
                    break
                M -= 1
                

solution()
