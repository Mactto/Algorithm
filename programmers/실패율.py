import sys
input = sys.stdin.readline


def solution(N, stages):
    total = len(stages)
    answer = []

    for i in range(1, N+1):
        c = stages.count(i)
        if c == 0:
            answer.append([0, i])
        else:
            answer.append([c / total, i])
        total = total - c
    answer = sorted(answer, key=lambda x: x[0], reverse=True)
    answer = [a[1] for a in answer]
    return answer


if __name__ == "__main__":
    N = int(input())
    stages = list(map(int, input().split()))
    print(solution(N, stages))
