def algorithm(N, K, price):
    result = 0
    for idx in range(N-1, -1, -1):
        value = K // price[idx]
        if value > 0:
            result += value
            K = K - (price[idx] * value)
    return result
            
    
if __name__ == "__main__":
    N, K = map(int, input().split())
    price = [int(input()) for _ in range(N)]
    print(algorithm(N, K, price))