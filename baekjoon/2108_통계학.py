from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
nums = list(int(input()) for _ in range(N))

nums.sort()

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
print(round(sum(nums) / N))

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(nums[N//2])

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
mode_dict = Counter(nums)
modes = [k for k, v in mode_dict.items() if v == max(mode_dict.values())]
modes = sorted(modes)
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(nums[N-1] - nums[0])
