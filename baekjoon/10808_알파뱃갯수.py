word = input()

# for i in range(97, 123):
#     if i == 122:
#         print(word.count(chr(i)))
#         break        
#     print(word.count(chr(i)), end=' ')

cnt = [0] * 26
for w in word:
    cnt[ord(w) - 97] += 1

print(cnt)