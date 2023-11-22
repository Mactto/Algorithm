from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_total = sum(queue1)
    q2_total = sum(queue2)

    while answer <= 300000:
        if answer == 300000:
            return -1

        if q1_total < q2_total:
            num = queue2.popleft()
            queue1.append(num)
            q1_total += num
            q2_total -= num
        elif q1_total > q2_total:
            num = queue1.popleft()
            queue2.append(num)
            q1_total -= num
            q2_total += num
        else:
            return answer

        answer += 1

    return answer