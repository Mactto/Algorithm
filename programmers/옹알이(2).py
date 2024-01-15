def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:
        for c in can:
            if c * 2 not in bab:
                bab = bab.replace(c, ' ')
                
        if bab.isspace():
            answer += 1
            
    return answer