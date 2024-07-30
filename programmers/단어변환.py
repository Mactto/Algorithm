from collections import deque

def get_convertable_words(standard, words):
    convert_able = []
    for word in words:
        len_dif = abs(len(standard) - len(word))
    
        if len(standard) > len(word):
            word += '!' * len_dif
        elif len(standard) < len(word):
            standard += '!' * len_dif
    
        dif_count = 0
        for i in range(len(standard)):
            if standard[i] != word[i]:
                dif_count += 1
                
        if dif_count < 2:
            convert_able.append(word)
    
    return convert_able

def solution(begin, target, words):
    answer = 0
    visited = {}
    
    for word in words:
        visited[word] = False
    
    if target not in visited:
        return answer

    queue = deque([])
    queue.append([0, begin])
    
    while queue:
        count, word = queue.popleft()
        
        if word == target:
            return count

        convertable = get_convertable_words(word, words)
        
        for w in convertable:
            if not visited[w]:
                queue.append([count + 1, w])
                visited[w] = True

    return answer