import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

word_dict = {}

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
word_list = [[w, c, len(w)] for w, c in word_dict.items()]
word_list = sorted(word_list, key=lambda x: x[0])
word_list = sorted(word_list, key=lambda x: (x[1], x[2]), reverse=True)

for w in word_list:
    print(w[0])