
import sys
input = sys.stdin.readline

def algorithm(loc):
    loc.sort()
    minus = [x for x in loc if x < 0]
    plus = [x for x in loc if x >= 0]
    print(minus, plus)



if __name__ == "__main__":
    N, M = map(int, input().split())
    loc = list(map(int, input().split()))
    print(algorithm(loc))
