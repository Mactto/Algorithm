from collections import deque

S = input()
T = input()

already_set = set()
queue = deque([T])

def bfs():
    while queue:
        string = queue.popleft()

        if len(string) == 0:
            continue

        if string == S:
            return 1

        if string[-1] == 'A':
            queue.append(string[:-1])
        if string[0] == 'B':
            string = string[1:]
            queue.append(string[::-1])

    return 0

print(bfs())