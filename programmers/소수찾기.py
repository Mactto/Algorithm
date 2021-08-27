from itertools import permutations
import sys
input = sys.stdin.readline


def decimal(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if decimal(num):
                answer.append(num)

    answer = list(set(answer))
    return len(answer)


if __name__ == "__main__":
    numbers = input().rstrip()
    print(solution(numbers))
