import sys
input = sys.stdin.readline

def algorithm():
    result = 0  # 필요한 테이프 개수 변수
    temp = 0    # 임시 변수

    for p in point:
        if temp < p:    # temp 변수보다 값이 클 경우 새로운 테이프 사용해야함
            result += 1 # 테이프 개수 + 1
            temp = p + L -1  # temp 업데이트
    return result       # 결과 반환

        

if __name__ == "__main__":
    N, L = map(int, input().split())
    point = list(map(int, input().split()))
    point.sort()
    print(algorithm())