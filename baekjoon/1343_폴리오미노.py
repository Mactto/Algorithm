import sys
input = sys.stdin.readline

def algorithm(board):
    i = 0
    while True:
        if i >= len(board):
            break

        if board[i:i+4] == 'XXXX':
            i += 4
            board = board.replace('X', 'A', 4)
        elif board[i:i+2] == 'XX':
            i += 2
            board = board.replace('X', 'B', 2)
        elif board[i] == '.':
            i += 1
    return board

if __name__ == "__main__":
    board = input().strip()
    if board.count('X') % 2 != 0:
        print('-1')
    else:
        print(algorithm(board))


# a = input()
# a = a.replace("XXXX", "AAAA")
# a = a.replace("XX", "BB")
# if a.count('X') >= 1:
#     a = -1
# print(a)