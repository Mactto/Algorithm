def solution(n, m, section):
    answer, paint = 0,0
    
    for s in section:
        if s>=paint:
            paint = s+m
            answer+=1
    
    return answer