import sys
input = sys.stdin.readline

def algorithm():
    price = 0
    for i in range(N):
        if i % 3 != 2:
            price += C[i]
    return price

if __name__ == "__main__":
    N = int(input())
    C = [int(input()) for _ in range(N)]
    C.sort(reverse=True)
    print(algorithm())