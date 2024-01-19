def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    for keys in keymap:
        for idx, key in enumerate(list(keys)):
            if key in key_dict:
                key_dict[key] = min(key_dict[key], idx+1)
            else:
                key_dict[key] = idx + 1

    for target in targets:
        total = 0
        for t in target:
            if t not in key_dict:
                total = -1
                break
            total += key_dict[t]
        answer.append(total)
        

    return answer