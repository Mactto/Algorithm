import sys
input = sys.stdin.readline

def solution(numbers, target):
    count = 0
    
    def bfs(numbers, target, idx=0):
        if idx < len(numbers):
            numbers[idx] *= 1
            bfs(numbers, target, idx+1)
            numbers[idx] *= -1
            bfs(numbers, target, idx+1)
        elif sum(numbers) == target:
            count += 1
    bfs(numbers, target)
    return count



if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    target = int(input())
    print(solution(0, 0))