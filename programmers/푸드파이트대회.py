def solution(food):
    answer = ''
    for idx, food_count in enumerate(food):
        if idx == 0:
            continue

        if food_count > 1:
            for _ in range(food_count // 2):
                answer += str(idx)

    reverse_food = ''.join(list(answer)[::-1])
    answer += '0'
    answer += reverse_food

    return answer