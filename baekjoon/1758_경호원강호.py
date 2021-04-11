import sys
input = sys.stdin.readline

def algorithm():
    tip.sort(reverse=True)
    result = 0

    for i in range(N):
        cal = tip[i] - ((i+1) - 1)
        if 0 < cal:
            result += cal
    return result

if __name__ == "__main__":
    N = int(input())
    tip = [int(input()) for _ in range(N)]
    print(algorithm())