game_to_need_people = {'Y': 2, 'F': 3, 'O': 4}

N, game = map(str, input().split())

result = 0
gather_count = 1
played_user_id_set = set()
for _ in range(int(N)):
    user_id = input()

    if user_id in played_user_id_set:
        continue

    gather_count += 1
    if gather_count == game_to_need_people[game]:
        gather_count = 1
        result += 1
    
    played_user_id_set.add(user_id)

print(result)