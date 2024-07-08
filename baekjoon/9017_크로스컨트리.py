T = int(input())

for _ in range(T):
    N = int(input())
    complete = list(map(int, input().split()))
    score_dict = {}
    
    complete_set = set(complete)
    for cs in complete_set:
        if complete.count(cs) == 6:
            score_dict[cs] = []
    
    score = 1
    for c in complete:
        if c in score_dict:
            score_dict[c].append(score)
            score += 1

    champion = 0
    temp_chanpion_value = 100000000
    chanpion_value = 100000000
    for key, value in score_dict.items():
        if sum(value[:4]) < chanpion_value:
            champion = key
            chanpion_value = sum(value[:4])
            temp_chanpion_value = sum(value[:5])
        elif sum(value[:4]) == chanpion_value:
            if sum(value[:5]) < temp_chanpion_value:
                champion = key
                temp_chanpion_value = sum(value[:5])

    print(champion)