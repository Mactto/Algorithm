import sys
input = sys.stdin.readline


def solution(s, n):
    answer = ''
    temp = list(s)
    for t in temp:
        if t == ' ':
            answer += ' '
            continue
        asc = ord(t)
        print(t, asc)
        if asc < 91 and asc + n > 90:
            asc -= 26
        elif asc < 123 and asc + n > 122:
            asc -= 26
        answer += chr(asc + n)
    return answer


if __name__ == "__main__":
    s = "a B z"
    n = 4
    print(solution(s, n))
