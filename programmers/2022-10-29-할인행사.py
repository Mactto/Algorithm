def solution(want, number, discount):
    limit = len(discount) - 10
    result = 0
    
    for i in range(len(discount)):
        flag = True
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) < number[j]:
                flag = False
                break
        if flag:
            result += 1
    
    return result
                
            
print(solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	
))