import sys
input = sys.stdin.readline

def bfs(point):
    queue = [point]

    while queue:
        c, r = queue.pop(0)
        land[c][r] = 0
        for k in range(8):
            ndx = c + dx[k]
            ndy = r + dy[k]
            if 0 <= ndx < h and 0 <= ndy < w:
                if land[ndx][ndy] == 1:
                    queue.append([ndx,ndy])
    

if __name__ == "__main__":
    w = h = 1
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    while w!=0 and h!=0:
        count = 0
        w, h = map(int, input().split())
        land = [list(map(int, input().strip().split())) for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if land[i][j] == 1:
                    count += 1
                    bfs([i,j])
        print(count)
