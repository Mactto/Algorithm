H, W = map(int, input().split())
wall_heights = list(map(int, input().split()))

most_heights_idx = wall_heights.index(max(wall_heights))
result = 0

# 왼쪽에서부터 가장 큰 벽까지 탐색
current_height = wall_heights[0]
for i in range(1, most_heights_idx + 1):
    if current_height <= wall_heights[i]:
        current_height = wall_heights[i]
    else:
        result += current_height - wall_heights[i]

current_height = wall_heights[-1]
# 오른쪽에서부터 가장 큰 벽까지 탐색
for i in range(len(wall_heights) - 1, most_heights_idx - 1, -1):
    if current_height <= wall_heights[i]:
        current_height = wall_heights[i]
    else:
        result += current_height - wall_heights[i]

print(result)