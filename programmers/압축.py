def solution(msg):
    answer = []
    dic = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 27)))

    while msg:
        length = len(msg)

        for i in range(length, 0, -1):
            word = msg[:i]

            if word in dic:
                answer.append(dic[word])
                if i != length:
                    dic[word + msg[i]] = len(dic) + 1

                msg = msg[i:]
                break
    return answer


if __name__ == "__main__":
    print(solution('TOBEORNOTTOBEORTOBEORNOT'))
