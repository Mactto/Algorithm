def solution(elements):
    element_length = len(elements)
    elements = elements * 2
    added_element_set = set()

    for i in range(elements):
        for j in range(elements):
            added_element_set.add(elements[j, j+i+1])

print(solution([7,9,1,1,4]))