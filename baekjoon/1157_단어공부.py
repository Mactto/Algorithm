word = input()
word = list(word.upper())

word_dict = {}

for w in word:
    if w in word_dict:
        word_dict[w] += 1
    else:
        word_dict[w] = 0

counts = [i for i in word_dict.values()]

if counts.count(max(counts)) > 1:
    print("?")
else:
    print(max(word_dict, key=word_dict.get))
