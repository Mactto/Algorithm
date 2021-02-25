import sys
input = sys.stdin.readline

def algorithm():
    boom = lazer = 0
    for g in game:
        if g == '(':
            boom += 1
        else:
            lazer += 1
    print(boom, lazer)
    if boom == lazer:
        return 'YES'
    else:
        return 'NO'

game = input().rstrip()
print(algorithm())