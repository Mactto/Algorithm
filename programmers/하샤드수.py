def solution(arr):
    return arr % sum(map(int, list(str(arr)))) == 0


if __name__ == "__main__":
    arr = 18
    print(solution(arr))
