from collections import Counter

S = list(map(str, input()))

value_dict = Counter(S)

delete_index = []

def delete_zero(delete_count: int):
    count = 0
    delete_index = []
    for i in range(len(S) - 1, -1, -1):
        if S[i] == '0':
            delete_index.append(i)
            count += 1

            if count == delete_count:
                return delete_index

def delete_one(delete_count: int):
    count = 0
    delete_index = []
    for i in range(len(S)):
        if S[i] == '1':
            delete_index.append(i)
            count += 1

            if count == delete_count:
                return delete_index

delete_index.extend(delete_zero(value_dict['0'] // 2))
delete_index.extend(delete_one(value_dict['1'] // 2))

result = ""
for i in range(len(S)):
    if i not in delete_index:
        result += S[i]

print(result)
