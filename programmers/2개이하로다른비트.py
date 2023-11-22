def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            number_to_binary = bin(number)[2:]
            binary_to_list = list(number_to_binary)
            idx = number_to_binary.rfind('0')
            if idx == -1:
                binary_to_list[0] = '0'
                answer.append(int('1' + ''.join(binary_to_list), 2))
            else:
                binary_to_list[idx] = '1'
                binary_to_list[idx+1] = '0'
                answer.append(int(''.join(binary_to_list), 2))
    
    return answer

solution([2,7])