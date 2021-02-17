import sys
input = sys.stdin.readline

def algorithm():
    result = 0          # 도착 후 가장 적은 기름값
    mini = 1000000001   # 현재 방문한 도시 중 가장 싼 기름값

    for idx in range(N-1):          
        if price[idx] < mini:       # 현재 도시의 기름값이 mini의 값보다 작을 경우
            mini = price[idx]       # mini에 현재 도시의 기름값을 저장
        result += mini * dist[idx]  # mini * 도로의 길이

    return result       # 결과 반환

if __name__ == "__main__":
    N = int(input())
    dist = list(map(int, input().split()))
    price = list(map(int, input().split()))
    print(algorithm())