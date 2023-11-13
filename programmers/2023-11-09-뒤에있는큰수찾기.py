def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            result[stack.pop(-1)] = numbers[i]
            
        stack.append(i)
    
    return result