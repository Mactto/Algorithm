def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        answer.append(max(i//n, i%n) + 1)

    return answer


def my_solution(n, left, right):
    temp = [i for i in range(1, n+1)]
    result = ''.join(str(x) for x in temp)
    
    for i in range(1, n):
        for j in range(i):
            temp[j] += 1
        result += ''.join(str(x)for x in temp)
    return list(map(int, result))[left: right+1]
    


# print(solution(3, 2, 5, [3,2,2,3]))
print(solution(4, 7, 14))
