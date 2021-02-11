'''
1. 서류 순위 순으로 정렬 후 면접 순위를 기준으로 선발한다.
2. 첫 번째에 있는 결과를 기준으로 잡고 아래 면접 결과를 보고 채용을 판별한다.
'''

import sys
input = sys.stdin.readline

def algorithm(grades):
    grades = sorted(grades, key=lambda x: x[0]) # 서류 결과를 기준으로 정렬
    result = 1                              
    st = grades.pop(0)[1]                       # 가장 첫번째 결과를 기준으로 잡음

    for g in grades:                            # 나머지 결과들을 반복
        if g[1] < st:                           # 기준보다 높은 순위일 경우 채용
            result += 1                     
            st = g[1]                           # 기준을 현재 결과로 변경
    print(result)         

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        grades = [list(map(int, input().strip().split())) for _ in range(N)]
        algorithm(grades)