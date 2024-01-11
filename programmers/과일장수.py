def solution(k, m, score):    
    answer = 0
    
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if i+(m-1) < len(score):
            answer += min(score[i:i+m]) * m
    
    return answer