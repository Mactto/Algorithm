import sys
input = sys.stdin.readline

def algorithm(m):
    for u in unit:
        print(m // u, end=' ')
        m = m % u

if __name__ == "__main__":
    T = int(input())
    unit = [25, 10, 5, 1]
    for _ in range(T):
        money = int(input())
        algorithm(money)
        print()