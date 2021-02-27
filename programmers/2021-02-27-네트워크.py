import sys
input = sys.stdin.readline

def solution(n, computers):
    visited = [False] * n
    result = 0

    def dfs(num):
        nonlocal result
        visited[num] = True

        for i in range(n):
            if not visited[i] and computers[num][i] == 1:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            result += 1
            dfs(i)

    return result


if __name__ == "__main__":
    n = int(input())
    computers = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, computers))