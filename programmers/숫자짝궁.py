def solution(X, Y):
    answer = ''

    X = list(map(int, X))
    Y = list(map(int, Y))

    for i in range(9, -1, -1):
        if i == 0 and min(X.count(i), Y.count(i)) > 0 and answer == '':
            answer += '0'
        else:
            answer += str(i) * min(X.count(i), Y.count(i))

    return answer if answer != '' else '-1'