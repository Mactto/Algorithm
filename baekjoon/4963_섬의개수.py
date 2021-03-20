import sys
from _collections import deque
input = sys.stdin.readline
    

if __name__ == "__main__":
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while True:
        queue = deque()
        count = 0
        w, h = map(int, input().split())
        if w == 0 and h == 0: break
        land = [list(map(int, input().strip().split())) for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if land[i][j] == 1:
                    count += 1
                    queue.append([i,j])

                    while queue:
                        c, r = queue.popleft()
                        land[c][r] = 0
                        for k in range(8):
                            ndx = c + dx[k]
                            ndy = r + dy[k]
                            if 0 <= ndx < h and 0 <= ndy < w:
                                if land[ndx][ndy] == 1:
                                    queue.append([ndx,ndy])
        print(count)
