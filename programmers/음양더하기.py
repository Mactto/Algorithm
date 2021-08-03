def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    print(answer)
    return answer


if __name__ == "__main__":
    absolutes = list(map(int, input().split()))
    signs = list(input().split())
    solution(absolutes, signs)
