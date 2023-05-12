import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())
    check_list = []
    time_list = [list(map(int, input().split())) for _ in range(N)]

    time_list.sort(key=lambda x: x[0])

    heapq.heappush(check_list, time_list[0][1])

    for i in range(1, N):
        if time_list[i][0] < check_list[0]:
            heapq.heappush(check_list, time_list[i][1])
        else:
            heapq.heappop(check_list)
            heapq.heappush(check_list, time_list[i][1])

    return len(check_list)

print(solution())