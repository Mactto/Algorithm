import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum_ranges = []
for _ in range(M):
    i, j = map(int, input().split())
    sum_ranges.append([i, j])

prefix_sum = [0] * N
prefix_sum[0] = nums[0]

for i in range(1, N):
    prefix_sum[i] = nums[i] + prefix_sum[i-1]

for i, j in sum_ranges:
    if i > 1:
        print(prefix_sum[j-1] - prefix_sum[i-2])
    else: 
        print(prefix_sum[j-1])
