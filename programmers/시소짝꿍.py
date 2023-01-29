import math
from collections import Counter

def solution(weights):
    answer = 0
    weights_count = Counter(weights)

    for _, c in weights_count.most_common():
        if c > 1:
            answer += int(math.factorial(c) / (math.factorial(c-2) * math.factorial(2)))    
    weights = list(set(weights))
    
    for weight in weights:
        for check in (3/4, 2/3, 2/4):
            if weight * check in weights:
                answer += weights_count[weight] * weights_count[weight * check]


    return answer