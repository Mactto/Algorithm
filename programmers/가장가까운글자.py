def solution(s):
    word_idx_dict = {}
    answer = []

    for idx, word in enumerate(s):
        if word not in word_idx_dict:
            answer.append(-1)
            word_idx_dict[word] = (idx + 1)
        else:
            answer.append((idx + 1) - word_idx_dict[word])
            word_idx_dict[word] = idx + 1

    return answer