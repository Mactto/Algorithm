def solution(k, score):
    answer = []
    
    highest = []
    for s in score:
        highest.append(s)
        highest.sort(reverse=True)
        answer.append(min(highest[:k]))

    return answer