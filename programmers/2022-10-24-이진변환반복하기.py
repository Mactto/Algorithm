def convert_binary(x):
    s = ""
    while True:
        if x // 2 == 0:
            if x % 2 == 1:
                s += "1"
            break
        s += str(x % 2)
        x = x // 2

    return s[::-1]


def solution(s):
    count = 0
    zero_count = 0
    
    while True:
        if s == "1":
            break
        count += 1
        
        zero_num = s.count("0")
        zero_count += zero_num
        s = convert_binary(len(s) - zero_num)

    return [count, zero_count]

# print(solution("110010101001"))
# print(solution("01110"))
print(solution("1111111"))