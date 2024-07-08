N = int(input())

result_set = set()
map_dict = {}

for i in range(1, N + 1):
    num = int(input())

    if i == num:
        result_set.add(num)
    else:
        map_dict[i] = num

for key in map_dict.keys():
    value = map_dict[key]
    if value in map_dict and key == map_dict[value]:
        result_set.add(key)
        result_set.add(map_dict[key])

print(len(result_set))
result = list(result_set)
result.sort()
for r in result:
    print(r)
