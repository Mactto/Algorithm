import sys
input = sys.stdin.readline

def algorithm():
    one = 0
    zero = 0

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i] == '1':
                one += 1
            else:
                zero += 1
    if s[-1] == '1': one += 1
    else: zero += 1
    return min(one, zero)
            
if __name__ == "__main__":
    s = input().strip()
    print(algorithm())