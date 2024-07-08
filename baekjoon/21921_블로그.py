
import sys
input = sys.stdin.readline


N, X = map(int, input().rstrip().split())
visited = list(map(int, input().rstrip().split()))

if max(visited) == 0:
    print("SAD")
else:
    value = sum(visited[:X])
    max_visited = value
    count = 1

    for i in range(X, N):
        value -= visited[i-X]
        value += visited[i]

        if max_visited < value:
            max_visited = value
            count = 1
        elif max_visited == value:
            count += 1

    print(max_visited)
    print(count)