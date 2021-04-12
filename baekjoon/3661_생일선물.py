# 강해져서 돌아온다

import sys
input = sys.stdin.readline

def algorithm():
    average = round(p / n)  # 선물가격 / 친구의 수 반올림 값
    remain = 0
    result = ''
    low_list = [e for e in enable if e < average]
    high_list = [e for e in enable if e >= average]

    # 낼 수 있는 금액이 작은 애들 먼저 뺴주기
    remain = p - sum(low_list)
    other_count = len(high_list)

    for hl in high_list:
        temp = remain // other_count
        if temp <= hl:
            result += str(temp) + ' '
            remain -= temp
            other_count -= 1
        else:
            return "IMPOSSIBLE"
    

    for ll in low_list:
        result += str(ll) + ' '
    
    return result

if __name__ == "__main__":
    T = int(input())    # 테스트 케이스
    for _ in range(T):
        p, n = map(int, input().split())    # 선물가격, 친구의 수
        enable = list(map(int, input().split()))    # 낼 수 있는 금액
        enable.sort()
        print(algorithm())
