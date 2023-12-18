import sys
input = sys.stdin.readline

N = int(input())
testee = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    result += 1

    if testee[i] > B:
        over = testee[i] - B
        if over % C == 0:
            result += over // C
        else:
            result += over // C + 1

print(result)