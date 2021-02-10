def algorithm(kilo):
    n = kilo // 5
    for i in range(n, -1, -1):
        result = kilo - (5 * i)
        if result % 3 == 0:
            return i + (result // 3)
    return -1
    
if __name__ == "__main__":
    kilo = int(input())
    print(algorithm(kilo))