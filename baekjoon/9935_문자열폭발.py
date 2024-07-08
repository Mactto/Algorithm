import sys
input = sys.stdin.readline

word = list(input().rstrip())
boom_word = list(input().rstrip())
stack = []

for w in word:
    stack.append(w)

    if ''.join(stack[-len(boom_word):]) == ''.join(boom_word):
        for _ in range(len(boom_word)):
            element = stack.pop()


if stack:
    print(''.join(stack))
else:
    print("FRULA")

