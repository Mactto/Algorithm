T = int(input())

def init_team_info(n: int):
    team_dict = {}
    for i in range(1, n+1):
        team_dict[i] = {
            "score": [],
            "submit_count": 0,
            "last_update_index": 0
        }

    return team_dict

def calculate_score(score_list: list):
    result = 0
    score_list = sorted(score_list, key=lambda x: x[1], reverse=True)
    calculated_quiz = set()
    for quiz_id, score in score_list:
        if quiz_id not in calculated_quiz:
            result += score
            calculated_quiz.add(quiz_id)
    
    return result


for _ in range(T):
    n, k, t, m = map(int, input().split())

    team_info = init_team_info(n)

    for k in range(m):
        i, j, s = map(int, input().split())

        team_info[i]["score"].append([j, s])
        team_info[i]["submit_count"] += 1
        team_info[i]["last_update_index"] = k

    evaluate_list = []
    for team_id, info in team_info.items():
        last_score = calculate_score(info["score"])
        evaluate_list.append([team_id, last_score, info["submit_count"], info["last_update_index"]])
    
    evaluate_list = sorted(evaluate_list, key=lambda x: [-x[1], x[2], x[3]])
    
    team_ranking = [el[0] for el in evaluate_list]
    print(team_ranking.index(t) + 1)