def solution(dirs):
    answer = []
    x, y = 0, 0
    temp = []
    commands = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}
    
    for cmd in dirs:
        print(x, y)
        nx, ny = commands[cmd]
        if -6 < x + nx < 6 and -6 < y + ny < 6:
            if [x, y, x+nx, y+ny] not in answer and [x+nx, y+ny, x, y] not in answer:
                answer.append([x, y, x+nx, y+ny])
            x += nx
            y += ny
    print(x, y)

    return len(answer)

if __name__ == "__main__":
    print(solution("UUUUDUDUDUUU"))