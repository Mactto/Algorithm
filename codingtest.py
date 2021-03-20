
import sys
input = sys.stdin.readline

'''1번
# 하나의 그래프로 생각하기
# 깊이 우선 탐색

def dfs(k, result):
    for c in combo:
        if k == c[0]:
            dfs(c[1], result + ' ' + c[1])
        else:
            return

def main():
    for k in K:
        dfs(k, str(k))

if __name__ == "__main__":
    K = input().rstrip().split()
    N = int(input())
    combo = [list(input().rstrip().split()) for _ in range(N)]
    main()
'''

''' 2번
def main():
    global array
    array = sorted(array, key=lambda x: x[1], reverse=True)     # 예약 시간 순으로 역순 정렬 후
    array = sorted(array, key=lambda x: x[0])                   # pc 순으로 정렬
    
    for pc in range(p):                    # pc 구분
        time = 0
        for a in array:                         # 예약 내역 하나씩 확인
            if (pc+1) == a[0]:                  # 예약 확인하고 있는 pc인지 확인
                if a[1] > h:                    # 예약 희망 시간이 영업 시간보다 많은 경우
                    pass                        # 예약 받지 않음
                else:
                    time += a[1]
                    if time == h:               # 예약 희망 시간이 영업 시간이랑 딱 맞는 경우
                        break                   # 다음 PC 검사
            else:                               # PC 번호가 다를 경우
                continue                           # 다음 PC 검사
        print(pc+1, time*1000)                  # 해당 pc의 최대 매출 출력
        

if __name__ == "__main__":
    p, n, h = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    main()

'''

# 1. 소마 위치에서 앞 뒤로 가장 가까운 땅콩 찾기
# 2. 만약 앞 뒤 땅콩의 거리가 동일할 경우 -> 두 경우 모두 살피기
# 3. 먹어야 하는 개수만큼만 먹기
# 너비우선탐색?

def main():
    queue = []
    result = []

    if E not in loc:
        mini = E
        point = 0
        for i in range(N):
            val = abs(E - loc[i])
            if val < mini:
                mini = val
                point = i
    else:

if __name__ == "__main__":
    N, M, E = map(int, input().split())
    loc = list(map(int, input().split()))
    main()







#SELECT o.buyer_id, o.buy_date, l.book_name, l.price FROM library l JOIN orderInfo o ON l.book_id = o.book_id WHERE l.book_name LIKE 'Looking with Elice' or o.buy_date BETWEEN '2020-07-27' AND '2020-07-31'