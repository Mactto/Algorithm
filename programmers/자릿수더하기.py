def solution(N):
    answer = 0
    for n in str(N):
        answer += int(n)
    return answer


if __name__ == "__main__":
    N = 123
    print(solution(N))
