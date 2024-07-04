import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = []

m = int(input())

for _ in range(m):
    commend = list(input().split())

    if commend[0] == 'L':
        if str1:
            str2.append(str1.pop())
    
    elif commend[0] == 'D':
        if str2:
            str1.append(str2.pop())
    
    elif commend[0] == 'B':
        if str1:
            str1.pop()

    elif commend[0] == 'P':
        str1.append(commend[1])

str1.extend(str2[::-1])
print(''.join(str1))
