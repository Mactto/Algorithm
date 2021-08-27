def grade(score):
    if 90 <= score:
        return 'A'
    elif 80 <= score:
        return 'B'
    elif 70 <= score:
        return 'C'
    elif 50 <= score:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    for i in range(len(scores)):
        temp = []
        score = 0
        own_score = scores[i][i]
        for j in range(len(scores[i])):
            temp.append(scores[j][i])
        if (max(temp) == own_score or min(temp) == own_score) and temp.count(own_score) == 1:
            temp.remove(own_score)
            score = sum(temp) / len(temp) 
        score = sum(temp) / len(temp)
        answer += grade(score)
    return answer


if __name__ == "__main__":
    print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))