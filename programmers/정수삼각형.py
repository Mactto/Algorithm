from collections import deque

def solution(triangle):
    answer = [[0 for _ in range(i)] for i in range(1, len(triangle)+1)]
    answer[0][0] = triangle[0][0]
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            answer[i+1][j] = max(answer[i][j] + triangle[i+1][j], answer[i+1][j])
            answer[i+1][j+1]  = max(answer[i][j] + triangle[i+1][j+1], answer[i+1][j+1])

    return max(answer[-1])