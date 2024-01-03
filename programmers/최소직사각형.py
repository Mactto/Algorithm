def solution(sizes):
    min_list = []
    max_list = []

    for size in sizes:
        min_list.append(min(size))
        max_list.append(max(size))

    return max(min_list) * max(max_list)