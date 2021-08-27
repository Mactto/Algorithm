def solution(arr1, arr2):
    answer = []
    for ar1, ar2 in zip(arr1, arr2):
        temp = []
        for a1, a2 in zip(ar1, ar2):
            temp.append(a1 + a2)
        answer.append(temp)
    return answer


if __name__ == "__main__":
    arr1 = [[1, 2], [2, 3]]
    arr2 = [[3, 4], [5, 6]]
    print(solution(arr1, arr2))
