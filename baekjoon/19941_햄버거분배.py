import sys
input = sys.stdin.readline

def algorithm():
    count = 0
    loc = list(location)
    for idx, s in enumerate(loc):
        if s == 'P':
            for j in range(idx-K, idx+K+1):
                if 0 <= j < N and loc[j] == 'H':
                    loc[j] = 'S'
                    count+=1
                    break
    return count

if __name__ == "__main__":
    N, K = map(int, input().split())
    location = input()
    print(algorithm())