def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    options = {'#': -1, '*': 2}

    answer = [0, 0, 0]
    flag = -1

    for idx, dart in enumerate(dartResult):
        if dart.isdigit():
            flag += 1
            if dart == '0':
                continue
            elif dartResult[idx+1].isdigit():
                answer[flag] = int(dart) * 10
                flag -= 1
            else:
                answer[flag] = int(dart)
        elif dart in 'SDT':
            answer[flag] **= bonus[dart]
        else:
            if dart == '*':
                answer[flag-1] *= options[dart]
            answer[flag] *= options[dart]
    return sum(answer)


if __name__ == "__main__":
    print(solution("1D2S#10S"))