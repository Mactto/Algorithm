import sys
input= sys.stdin.readline

def algorithm(S, T):
    while len(S) != len(T):
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            T = T[::-1]

    return 1 if S == T else 0        

if __name__ == "__main__":
    S = list(input().strip())
    T = list(input().strip())
    print(algorithm(S, T))
