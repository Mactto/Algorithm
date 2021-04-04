import sys
input = sys.stdin.readline

def algorithm():
    ju = []
    result = 0
    for i in range(N-1):
        if date[i] <= date[i+1]:
            ju.append(date[i])
        else:
            for _ in range(len(ju)):
                result += date[i] - ju.pop(0)
    for j in ju:
        result += date[len(date)-1] - j
    return result

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        N = int(input())
        date = list(map(int, input().split()))
        print(algorithm())