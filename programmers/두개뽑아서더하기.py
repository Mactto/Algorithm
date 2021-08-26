import sys
input = sys.stdin.readline

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sort(set(answer))

if __name__ == "__main__":
    numbers = [1,2]
    print(solution(numbers))