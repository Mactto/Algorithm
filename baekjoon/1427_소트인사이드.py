import sys
input = sys.stdin.readline

N = int(input())
N = list(str(N))
N.sort(reverse=True)
print(''.join(N))
