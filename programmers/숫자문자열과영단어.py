dic = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def solution(s):
    answer = ''

    while s:
        if s[0].isdigit():
            answer += s[0]
            s = s[1:]
        else:
            for i in range(1, len(s)+1):
                if s[:i] in dic:
                    answer += str(dic[s[:i]])
                    s = s[i:]

    return answer


if __name__ == "__main__":
    s = input()
    print(solution(s))
