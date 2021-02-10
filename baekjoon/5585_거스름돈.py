def algorithm(change):
    c_list = [500, 100, 50, 10, 5, 1]
    result = 0
    for c in c_list:
        result += change // c
        change = change % c
    return result
    
if __name__ == "__main__":
    pay = int(input())
    print(algorithm(1000-pay))