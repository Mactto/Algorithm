def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solution(a, b)
