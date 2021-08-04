import sys
input = sys.stdin.readline

def solution(left, right):
    answer = 0

    for n in range(left, right+1):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count % 2 == 0:
            answer += n
        else:
            answer -= n
    return answer    

if __name__ == "__main__":
    left = int(input())
    right = int(input())
    print(solution(left, right))