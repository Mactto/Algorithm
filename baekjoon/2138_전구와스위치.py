import sys
input = sys.stdin.readline

def switch(idx, state):
    for i in range(idx-1, idx+2):
        if -1 < i and i < N:
            if state[i] == '0':
                state[i] = '1'
            else:
                state[i] = '0'
    return state

def zeroAlgorithm(state):
    count = 0
    for idx in range(1, N):
        if state[idx-1] != answer[idx-1]:
            state = switch(idx, state)
            count += 1
    if ''.join(state) == answer:
        return count
    else:
        return -1

def zeroSwitchAlgorithm(state):
    count = 1
    state = switch(0, state)
    for idx in range(1, N):
        if state[idx-1] != answer[idx-1]:
            state = switch(idx, state)
            count += 1
    if ''.join(state) == answer:
        return count
    else:
        return -1

if __name__ == "__main__":
    N = int(input())
    state = list(input().strip())
    answer = input().strip()
    ans1 = zeroAlgorithm(state[:])
    ans2 = zeroSwitchAlgorithm(state[:])

    if ans1 > 0 and ans2:
        print(min(ans1, ans2))
    elif ans1 > 0 and ans2 == -1:
        print(ans1)
    elif ans1 == -1 and ans2 > 0:
        print(ans2)
    else:
        print(-1)