from collections import deque
# deque로 풀기
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
    
# dfs로 풀기
def solution2(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, val):
        if idx == n:
            if val == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx+1, val + numbers[idx])
            dfs(idx+1, val - numbers[idx])
    dfs(0, 0)
    return answer

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    target = int(input())
    print(solution(numbers, target))
    print(solution2(numbers, target))