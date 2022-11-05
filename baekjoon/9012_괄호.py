import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        flag = True
        left_bracket = 0
        right_bracket = 0
        value = sys.stdin.readline().rstrip()

        for v in value:
            if v == '(':
                left_bracket += 1
            elif v == ')':
                right_bracket += 1
            
            if left_bracket < right_bracket:
                flag = False
        if flag and left_bracket == right_bracket:
            print("YES")
        else:
            print("NO")

solution()