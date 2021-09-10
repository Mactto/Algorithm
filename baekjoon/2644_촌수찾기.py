from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
target1, target2 = map(int, input().split())
M = int(input())
relations = [list(map(int, input().split())) for _ in range(M)]


def bfs(v, count):
    queue = deque()
    queue.append([v, count])
    visited = [False for _ in range(N+1)]

    while queue:
        temp, answer = queue.popleft()

        if temp == target2:
            return answer

        for v1, v2 in relations:
            if not visited[temp]:
                if v1 == temp:
                    queue.append([v2, answer+1])
                if v2 == temp:
                    queue.append([v1, answer+1])
        visited[temp] = True
    return -1


print(bfs(target1, 0))
