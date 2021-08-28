def solution(table, languages, preference):
    answer = [0 for _ in range(len(table))]
    table = sorted(table, key=lambda x: x[0])

    for idx, t in enumerate(table):
        t = t.split()
        for i in range(len(languages)):
            if languages[i] in t:
                score = 6 - t.index(languages[i])
                answer[idx] += score * preference[i]

    return table[answer.index(max(answer))].split()[0]


if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    print(solution(table, languages, preference))
