import sys
input = sys.stdin.readline
import itertools

def solution(word):
    answer = []
    words = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(5):
        answer += list(map(''.join, itertools.product(words, repeat=i+1)))

    answer.sort()
    print(answer)
    return answer.index(word) + 1

print(solution('AAAE'))