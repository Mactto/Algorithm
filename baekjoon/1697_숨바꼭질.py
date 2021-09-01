from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
result = 0
queue.append([N, 0])
visited = set()


def bfs():
    global queue, result, visited
    while queue:
        point, time = queue.popleft()
        if point not in visited:
            visited.add(point)

            time += 1
            if point == K:
                result = time - 1
                break
            else:
                if point < K:
                    queue.append([point * 2, time])
                    queue.append([point + 1, time])
                queue.append([point - 1, time])


bfs()
print(result)
