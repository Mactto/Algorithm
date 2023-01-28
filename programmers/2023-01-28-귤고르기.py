from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine_count = Counter(tangerine).most_common()

    for tan in tangerine_count:
        answer += 1
        _, count = tan
        if k - count <= 0:
            return answer
        k -= count


print(solution(2, [1,1,1,1,2,2,2,3]))