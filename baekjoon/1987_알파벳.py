import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]
alphabet = set()
alphabet.add(board[0][0])
result = 0

def dfs(pos, count):
    global alphabet, result
    x, y = pos
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in alphabet:
            alphabet.add(board[ny][nx])
            dfs([nx, ny], count+1)
            alphabet.remove(board[ny][nx])
dfs([0,0], 1)
print(result)