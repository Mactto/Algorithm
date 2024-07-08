import copy
from collections import deque

N, M = map(int, input().split())

game_board = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(board, dx, dy):
    ...

def solution():
    queue = deque()

    for i in range(N):
        for j in range(M):
            if game_board[i][j] == "B":
                blue_point = (i, j)
            if game_board[i][j] == "R":
                visited[i][j] = True
                red_point = (i, j)
        queue.append(red_point, blue_point, 0)

    while queue:
    

            