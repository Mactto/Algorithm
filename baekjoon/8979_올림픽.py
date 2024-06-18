N, K = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

rating = [0 for _ in range(N+1)]

country = sorted(country, key=lambda x: x[3], reverse=True)
country = sorted(country, key=lambda x: x[2], reverse=True)
country = sorted(country, key=lambda x: x[1], reverse=True)

rating[country[0][0]] = 1
for i in range(1, N):
    prev_cn, prev_g, prev_s, prev_b = country[i-1]
    cn, g, s, b = country[i]

    if prev_g == g and prev_s == s and prev_b == b:
        rating[cn] = rating[prev_cn]
    else:
        rating[cn] = i + 1

print(rating[K])