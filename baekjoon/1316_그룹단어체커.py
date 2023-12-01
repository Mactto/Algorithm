import sys
input = sys.stdin.readline

N = int(input())

def check_group_word(word: str):
    word_set = set()

    current = ""
    for w in list(word):
        if current != w:
            if w in word_set:
                return 0
            word_set.add(w)
        current = w

    return 1

    

count = 0
for _ in range(N):
    word = input()
    count += check_group_word(word)
print(count)