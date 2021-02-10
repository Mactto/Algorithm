def algorithm(info):
    count = 0
    limit = 0
    for i in info:
        if i[0] >= limit:
            limit = i[1]
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    info = [list(map(int, input().split())) for _ in range(n)]
    info = sorted(info, key=lambda x: x[0])
    info = sorted(info, key=lambda x: x[1])
    print(algorithm(info))