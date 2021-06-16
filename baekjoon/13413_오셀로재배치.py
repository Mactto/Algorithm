import sys
input = sys.stdin.readline

def algorithm():
    temp = []
    for i in range(N):
        if goal[i] != state[i]:
            temp.append(state[i])
    w, b = temp.count('W'), temp.count('B')
    if w >= b:
        return w
    else:
        return b 

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        goal = input()
        state = input()
        print(algorithm())
