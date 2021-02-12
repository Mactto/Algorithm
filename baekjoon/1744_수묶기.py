import sys
input = sys.stdin.readline

def algorithm():
    result = 0
    zero = sequence.count(0)
    bundle = []
    minus = []
    sets = set()
    sequence.sort(reverse=True)

    for s in sequence:
        if s in sets:
            result += s
        elif s == 1:
            result += s
        elif s == 0:
            zero += 1
        elif s < 0:
            continue
        else:
            bundle.append(s)
        if len(bundle) == 2:
            result += bundle[0] * bundle[1]
            bundle = []
        sets.add(s)

    minus.sort()
    for m in minus:
        if zero > 0:
            zero -= 1
            continue
        else:
            result += m
    if len(bundle) != 0:
        return result + bundle[0]
    return result
            
if __name__ == "__main__":
    N = int(input())
    sequence = [int(input()) for _ in range(N)]
    print(algorithm())