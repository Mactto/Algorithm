def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

N = int(input())
building = list(map(int, input().split()))

result = 0
for i in range(N):
    count_can_see = 0

    last_slope = -int(1e9)
    # 왼쪽 건물들을 탐색
    for l in range(i-1, -1, -1):
        current_slope = slope(i, building[i], l, building[l])
        if current_slope > last_slope:
            count_can_see += 1
            last_slope = current_slope
        else:
            break
    
    # 오른쪽 건물들을 탐색
    last_slope = -int(1e9)
    for r in range(i+1, N):
        current_slope = slope(i, building[i], r, building[r])
        if current_slope > last_slope:
            count_can_see += 1
            last_slope = current_slope
        else:
            break
    
    result = max(result, count_can_see)

print(result)
