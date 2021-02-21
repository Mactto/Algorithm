import sys
input = sys.stdin.readline

def algorithm():
    result = 0
    for i in range(N-1, 0, -1):                     # 가장 높은 레벨에서부터 탐색
        if score[i-1] >= score[i]:                  # 이전 레벨의 부여 점수가 더 높거나 같은 경우
            result += score[i-1] - (score[i]-1)     # result에 감소시켜야 할 수 더함
            score[i-1] = score[i]-1                 # 이전 레벨의 부여 점수를 현재 레벨 부여 점수-1 만큼 설정
    return result                                   # 총 감소시킨 수 반환


if __name__ == "__main__":
    N = int(input())
    score = list(int(input()) for _ in range(N))
    print(algorithm())