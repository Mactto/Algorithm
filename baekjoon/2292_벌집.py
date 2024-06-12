import sys
input = sys.stdin.readline

N = int(input())

last = 1
count = 1

while N > last:
    last = last + (6 * count)
    count += 1

print(count)