def algorithm(time):
    result = add = 0
    time.sort()
    for t in time:
        add = add + t
        result += add
    return result

if __name__ == "__main__":
    people = int(input())
    time = list(map(int, input().split()))
    print(algorithm(time))