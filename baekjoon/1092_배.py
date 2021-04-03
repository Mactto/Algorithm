import sys
import heapq
input = sys.stdin.readline

def algorithm(weight):
    if limit[0] < weight[0]:
        return -1
    else:
        count = 0
        while weight:
            count += 1
            for l in limit:
                for i in range(len(weight)):
                    if l >= weight[i]:
                        weight.pop(i)
                        break
        return count

if __name__ == "__main__":
    N = int(input())
    limit = list(map(int, input().split()))
    M  = int(input())
    weight = list(map(int, input().split()))
    limit.sort(reverse=True)
    weight.sort(reverse=True)
    print(algorithm(weight))
