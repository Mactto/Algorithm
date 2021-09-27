import sys
input = sys.stdin.readline

T = int(input())
testcase = [list(map(int, input().split())) for _ in range(T)]

for idx, test in enumerate(testcase):
    answer = 0
    for t in test:
        if t % 2 != 0:
            answer += t
    print("#" + str(idx+1) + " " + str(answer))
