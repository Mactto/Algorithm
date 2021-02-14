import sys
input = sys.stdin.readline

def algorithm():
    value = result = count = zero = 0
    overlap = set()
    sequence.sort(reverse=True)

    while sequence:
        s = sequence.pop(0)
        if s > 1:
            if count == 1:
                result += value * s
                count = 0
            elif s not in overlap and count == 0:
                value = s
                count += 1
            else:
                result += s
            overlap.add(s)
        elif s == 1:
            result += s
        elif s == 0:
            zero += 1
        else:
            sequence.append(s)
            sequence.sort()
            break
    
    if count == 1:
        result += value
        count = 0

    for s in sequence:
        if s in overlap:
            if zero != 0:
                result += s
        elif count == 0:
            value = s
            count += 1
        else:
            result += value * s
            count = 0
    
    if count == 1 and zero == 0:
        result += value

                
    return result

if __name__ == "__main__":
    N = int(input())
    sequence = [int(input()) for _ in range(N)]
    print(algorithm())