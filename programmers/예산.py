import sys
input = sys.stdin.readline

def solution(d, budget):
    d.sort()
    count = 0
    for i in d:
        if budget < i:
            break
        budget -= i
        count += 1
        
    return count

if __name__ == "__main__":
    d = list(map(int, input().split()))
    budget = int(input())
    print(solution(d, budget))