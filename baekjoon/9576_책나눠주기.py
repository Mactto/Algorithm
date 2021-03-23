import sys
input = sys.stdin.readline

def algorithm():
    count = 0
    check_list = [1] * (N+1)
    for a, b in num_list:
        for i in range(b, a-1, -1):
            if check_list[i] == 1:
                count += 1
                check_list[i] = 0
                break
    return count

if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        N, M = map(int, input().split())
        num_list = [list(map(int, input().split())) for _ in range(M)]
        num_list = sorted(num_list, key=lambda x: x[0], reverse=True)
        print(algorithm())