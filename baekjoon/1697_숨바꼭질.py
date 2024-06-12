from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(1000001)]

def bfs():
    queue = deque()
    queue.append([N, 0])
    visited[0] = True

    while True:
        position, prev_time = queue.popleft()
        
        
        

print(bfs())