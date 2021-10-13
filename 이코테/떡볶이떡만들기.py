import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ricecake_heights = list(map(int, input().split()))

def binary_search(array, target ,start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for a in array:
            if a > mid:
                total += a - mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result
start = 0
end = max(ricecake_heights)
print(binary_search(ricecake_heights, M, start, end))
