N = int(input())
balls = list(input())

def count_move_ball(typ: str):
    result = 0
    temp = 0
    for i in range(N-1):
        if balls[i] == typ:
            temp += 1
            if balls[i] != balls[i+1]:
                result += temp
                temp = 0
    return result

print(min(count_move_ball('B'), count_move_ball('R')))