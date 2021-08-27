import sys
input = sys.stdin.readline


def check(s):
    stack = []
    for t in s:
        if t == '(' or t == '{' or t == '[':
            stack.append(t)
        else:
            if not stack:
                return False
            x = stack.pop()
            if t == ')' and x != '(':
                return False
            if t == '}' and x != '{':
                return False
            if t == ']' and x != '[':
                return False
    return len(stack) == 0


def solution(s):
    answer = 0
    for t in s:
        temp, s = s[0], s[1:]
        s = s + temp
        if check(s):
            answer += 1
    return answer


if __name__ == "__main__":
    s = "}]()[{"
    print(solution(s))
