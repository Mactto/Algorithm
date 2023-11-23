import sys
from collections import deque
input = sys.stdin.readline

X = int(input())

queue = deque([(X, 0)])

while True:
    x, count = queue.popleft()

    if x == 1:
        print(count)
        break
    elif x > 1:
        count += 1
        if x % 3 == 0:
            queue.append((x // 3, count))
        if x % 2 == 0:
            queue.append((x // 2, count))
        queue.append((x - 1, count))
