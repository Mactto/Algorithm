import sys
input = sys.stdin.readline

def solution(people, limit):
    people.sort()
    result = 0

    i, j = 0, len(people)-1
    while i<=j:
        result+=1
        if people[j]+people[i]<=limit:
            i=i+1
        j=j-1
    return result

if __name__ == "__main__":
    people = list(map(int, input().split()))
    limit = int(input())
    print(solution(people, limit))