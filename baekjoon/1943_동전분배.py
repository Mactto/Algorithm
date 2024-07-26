def check(coins: list):
    left = 0
    left_sum = coins[0]
    right = len(coins) - 1
    right_sum = coins[-1]

    while left < right:
        if left_sum == right_sum:
            if left == right - 1:
                return 1
            elif right - left < 2:
                return 0
            else:
                left += 1
                left_sum += coins[left]
        elif left_sum < right_sum:
            left += 1
            left_sum += coins[left]
        elif left_sum > right_sum:
            right -= 1
            right_sum += coins[right]
    
    return 0

for _ in range(3):
    
    N = int(input())
    coins = []
    for _ in range(N):
        coin, count = map(int, input().split())
        
        if count % 2 != 0:
            temp = [coin for _ in range(count)]
            coins.extend(temp)
    
    if len(coins) == 0:
        print(1)
    else:
        coins.sort()
        print(check(coins))