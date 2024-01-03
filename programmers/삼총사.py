from itertools import combinations

def solution(number):
    answer = 0

    student_combi = combinations(number, 3)
    for sc in student_combi:
        if sum(sc) == 0:
            answer += 1

    return answer