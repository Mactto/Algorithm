N, K = map(int, input().split())
a = list(map(int, input().split()))


count_dict = {}
max_length = 0
temp_length = 0

for i in range(N):
    temp_length += 1

    if a[i] in count_dict:
        if count_dict[a[i]] + 1 > K:
            count_dict = {}
            max_length = max(max_length, temp_length - 1)
            temp_length = 0
        else:
            count_dict[a[i]] += 1
    else:
        count_dict[a[i]] = 1

    

print(max_length)