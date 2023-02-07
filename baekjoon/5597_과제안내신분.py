def solution():
    submit_list = [i for i in range(1, 31)]
    for _ in range(28):
        student = int(input())
        if student in submit_list:
            submit_list.remove(student)
        
    for sl in submit_list:
        print(sl)

solution()