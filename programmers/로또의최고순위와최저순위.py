import sys
input = sys.stdin.readline

grade = {
    6: 1,
    5: 2,
    4: 3,
    3: 4,
    2: 5,
    1: 6,
    0: 6
}

def solution(lottos, win_nums):
    count = 0
    zero_count = lottos.count(0)

    for w in win_nums:
        if w in lottos:
            count += 1
    return [grade[count+zero_count], grade[count]]


if __name__ == "__main__":
    lottos = list(map(int, input().split()))
    win_nums = list(map(int, input().split()))
    print(solution(lottos, win_nums))
