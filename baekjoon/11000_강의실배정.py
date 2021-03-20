import sys
import heapq
input = sys.stdin.readline

def algorithm():
    for i in range(N):
        if len(arr) != 0 and arr[0] <= time[i][0]:
            heapq.heappop(arr)
        heapq.heappush(arr, time[i][1])

    return len(arr)

    

if __name__ == "__main__":
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    time.sort(key=lambda x: x[0])
    print(algorithm())
    