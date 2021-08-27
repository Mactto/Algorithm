def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(solution(arr))
