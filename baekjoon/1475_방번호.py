sets = [0] * 10

room_number = list(input())

for number in room_number:
    sets[int(number)] += 1

sets[6], sets[0] = sets[6] + sets[9], 0

if sets[6] > 1:
    sets[6] = sets[6] // 2

print(max(sets))