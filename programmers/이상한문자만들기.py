
def solution(s):
    answer = ''
    words = s.split(" ")
    for w in words:
        print(w)
        temp = list(w)
        for idx, t in enumerate(temp):
            if idx % 2 == 0:
                answer += t.upper()
            else:
                answer += t.lower()
        answer += ' '
    return answer[:-1]


if __name__ == "__main__":
    s = "try hello world"
    print(solution(s))
