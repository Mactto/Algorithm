import heapq

def solution(operations):
    count_dict = {}
    min_heap = []
    max_heap = []
    
    for operation in operations:
        op, number = operation.split()
        number = int(number)
        if op == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -1 * number)
            
            if number in count_dict:
                count_dict[number] += 1
            else:
                count_dict[number] = 1
        elif op == "D":
            if len(count_dict) == 0:
                continue

            if number == -1:
                while True:
                    n = heapq.heappop(min_heap)
                    
                    if n in count_dict:
                        count_dict[n] -= 1
                        if count_dict[n] == 0:
                            del count_dict[n]
                        break
            else:
                while True:
                    n = heapq.heappop(max_heap)
                    n = n * -1
                    
                    if n in count_dict:
                        count_dict[n] -= 1
                        if count_dict[n] == 0:
                            del count_dict[n]
                        break
    answer = list(count_dict.keys())
    answer.sort()
    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))