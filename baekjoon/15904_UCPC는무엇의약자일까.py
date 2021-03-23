import sys
input = sys.stdin.readline

def algorithm(text):
    i = 0
    for a in alp:
        if a in s:
            i += 1
            s = s[s.index(a) + 1:]
        else:
            print('I hate UCPC')
            break
    if i == 4:
        print('I love UCPC')

if __name__ == "__main__":
    text = input().rstrip()
    ucpc = ['U', 'C', 'P', 'C']
    print(algorithm(text))