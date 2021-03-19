import sys
input = sys.stdin.readline

def algorithm(text):
    for i in range(len(ucpc)):
        if ucpc[i] in text:
            idx = text.find(ucpc[i])
            text = text[idx + 1:]
        else:
            return "I hate UCPC"
    return "I lova UCPC"

if __name__ == "__main__":
    text = input().rstrip()
    ucpc = ['U', 'C', 'P', 'C']
    print(algorithm(text))