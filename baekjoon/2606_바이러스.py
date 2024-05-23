from collections import deque

N = int(input())
M = int(input())

networking = {}

for n in range(1, N + 1):
    networking[n] = set()

for _ in range(M):
    c1, c2 = map(int, input().split())
    networking[c1].add(c2)
    networking[c2].add(c1)

def bfs(com_num):
    queue = deque([com_num])
    zombie_pc = set()
    zombie_pc.add(com_num)

    while queue:
        computer = queue.popleft()

        for c in networking[computer]:
            if c not in zombie_pc:
                queue.append(c)
                zombie_pc.add(c)

    return len(zombie_pc) - 1

print(bfs(1))