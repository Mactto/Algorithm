def solution(num, k):
    try:
        return list(str(num)).index(str(k))+1
    except:
        return -1 

print(solution(123456, 7))