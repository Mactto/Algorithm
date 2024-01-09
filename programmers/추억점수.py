def solution(name, yearning, photo):
    answer = []
    name_to_yearning = {}

    for name, yearning in zip(name, yearning):
        name_to_yearning[name] = yearning

    for p in photo:
        total_yearning = 0
        for name in p:
            if name in name_to_yearning:
                total_yearning += name_to_yearning[name]
        answer.append(total_yearning)

    return answer