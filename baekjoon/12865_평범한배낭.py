
N, V = map(int, input().split())

weight_list = []
value_list = []

for _ in range(N):
    weight, value = map(int, input().split())
    weight_list.append(weight)
    value_list.append(value)

from itertools import combinations

def find_combinations(weights, values, weight_limit):
    valid_combinations = []

    for r in range(1, N + 1):
        for combo in combinations(zip(weights, values), r):
            combo_weights, combo_values = zip(*combo)
            if sum(combo_weights) <= weight_limit:
                valid_combinations.append((combo_weights, combo_values))

    return valid_combinations

# Example usage
weights = [6, 4, 3, 5]
values = [13, 8, 6, 12]
weight_limit = 7

result = 0
combinations = find_combinations(weight_list, value_list, V)
for combo_weights, combo_values in combinations:
    result = max(sum(combo_values), result)
print(result)
