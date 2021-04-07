import sys
input = sys.stdin.readline

def algorithm():
    end_m = 3
    end_d = 1
    month = 3
    day = 1
    cnt = 0

    while True:
        if 11 <= month:
            if 11 != month or day == 31:
                break
        for i in range(N):
            if flower[i][0] <= month:
                if flower[i][0] != month or flower[i][0] <= day:
                    if end_m <= flower[i][2]:
                        if end_m != flower[i][2] or end_d <= flower[i][3]:
                            end_m = flower[i][2]
                            end_d = flower[i][3]
        if month == end_m and day == end_d:
            cnt = 0
            break
        month = end_m
        day = end_d
        cnt += 1
    return cnt



if __name__ == "__main__":
    N = int(input())
    flower = [list(map(int, input().split())) for _ in range(N)]
    print(algorithm())