def solution(phone_number):
    return '*' * len(phone_number[:-4]) + phone_number[-4:]


if __name__ == "__main__":
    phone_number = "01033334444"
    print(solution(phone_number))
