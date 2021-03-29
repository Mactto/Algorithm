import sys
input = sys.stdin.readline

def algorithm():
    max_wegiht = 0
    result = 0

    for n in range(N):
        for i in info:
            if i[1] == n:
                if max_wegiht - i[2] >= 0:
                    max_wegiht -= i[2]
                else:
                    max_wegiht = 0
                print('sub', i, max_wegiht)
            if i[0] == n and max_wegiht < C:
                if max_wegiht + i[2] <= C:
                    result += i[2]
                    max_wegiht += i[2]
                else:
                    result += C - max_wegiht
                    max_wegiht = C
                print('add', i, max_wegiht)

    return result


if __name__ == "__main__":
    N, C = map(int, input().split())
    M = int(input())
    info = [list(map(int, input().split())) for _ in range(M)]
    info = sorted(info, key=lambda x: x[1])
    info = sorted(info, key=lambda x: x[0])
    # print(N, C)
    # print(M)
    # print(info)
    print(algorithm())
