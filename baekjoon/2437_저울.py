import sys
input = sys.stdin.readline

# 처음 푼 풀이
'''
def algorithm():
    from itertools import combinations
    enable = set(weights)
    for i in range(2, N+1):
        combi = list(combinations(weights, i))
        for c in combi:
            enable.add(sum(c))
    
    for i in range(1, max(enable)):
        if i not in enable:
            return i
'''        

# 수정 풀이
def algorithm():
    result = 1
    weights.sort()

    for i in weights:
        if result<i:
            break
        result+=i
    return result    

if __name__ == "__main__":
    N = int(input())
    weights = list(map(int, input().split()))
    print(algorithm())
    

if __name__ == "__main__":
    N = int(input())
    weights = list(map(int, input().split()))
    print(algorithm())
