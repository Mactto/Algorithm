from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

relation = [0 for _ in range(n + 1)]
relation_dict = {}

for i in range(1, n+1):
    relation_dict[i] = []

for _ in range(m):
    x, y = map(int, input().split())
    relation_dict[x].append(y)
    relation_dict[y].append(x)

def bfs(p1, p2):
    queue = deque()
    queue.append([p1, 0])

    while queue:
        target, count = queue.popleft()

        if target == p2:
            return relation[p2]

        for r in relation_dict[target]:

            if relation[r] == 0:
                relation[r] = count + 1
                queue.append([r, count + 1])
    
    return -1
            

print(bfs(p1, p2))
