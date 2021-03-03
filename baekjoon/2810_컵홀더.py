import sys
input = sys.stdin.readline

def algorithm():
    i, count = 0, 1

    while i < N: 
        if seat[i] == 'L':
            i += 2
        else:
            i += 1
        count += 1
    return min(count, N)

if __name__ == "__main__":
    N = int(input())
    seat = input()
    print(algorithm())