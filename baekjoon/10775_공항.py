import sys
input = sys.stdin.readline

def algorithm():
    gate = set()
    result = 0

    for d in docking:
        if d not in gate:
            result += 1
            gate.add(d)
    return result

if __name__ == "__main__":
    G = int(input())
    P = int(input())
    docking = [int(input()) for _ in range(P)]
    print(algorithm())