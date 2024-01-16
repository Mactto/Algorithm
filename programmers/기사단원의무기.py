def measure(num):
    count = 0

    for i in range(1, int(num**(1/2))+1):
        if num % i == 0:
            if i ** 2 == num:
                count += 1
            else:
                count += 2
    return count

def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        m = measure(i)
        if m > limit:
            answer += power
        else:
            answer += measure(i)

    return answer