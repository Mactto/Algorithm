import sys
input = sys.stdin.readline

def algorithm():                                                
    if (V % P) > L:                                             # 만약 남는 기간이 이용 가능 기간보다 긴 경우
        return (V // P * L) + L                                 # 사용 할 수 있는 기간 + 이용 가능 기간 반환
    else:                                                       # 그 외 경우
        return (V // P * L) + (V % P)                           # 사용 할 수 있는 기간 + 남는 기간

if __name__ == "__main__":
    case = 1                                                    # 몇 번째 Case인지 구분
    while True:                                                 # 무한 루프
        L, P, V = map(int, input().split())                     # L, P, V를 입력 받음
        if (L == P and P == V and V == 0):                      # 만약 0, 0, 0이 입력되면 무한루프 탈출
            break                       
        print("Case " + str(case) + ": " + str(algorithm()))    # 결과 출력
        case += 1                                               # Case 증가