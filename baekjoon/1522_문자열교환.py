string = list(input())
a_count = string.count('a')
string += string

result = int(1e9)
for i in range(len(string) - a_count):
    result = min(result, string[i:i+a_count].count('b'))

print(result)