from collections import deque

class WordGame2:
    def __init__(self, W: list[str]):
        self.word = W
        self.word_heap_dict: dict[deque] = {}
        self.word_count_dict: dict[int] = {}

        for w in W:
            self.word_heap_dict[w] = deque()
            self.word_count_dict[w] = 0
    
    def game(self, k: int):
        min_result = int(1e9)
        max_result = 0

        for i in range(len(self.word)):
            self.word_count_dict[self.word[i]] += 1
            self.word_heap_dict[self.word[i]].append(i)

            if self.word_count_dict[self.word[i]] == k:
                self.word_count_dict[self.word[i]] -= 1
                first = self.word_heap_dict[self.word[i]].popleft()
                min_result = min(min_result, i - first + 1)
                max_result = max(max_result, i - first + 1)

        if min_result == int(1e9) and max_result == 0:
            return [-1]
        return [min_result, max_result]


T = int(input())

for _ in range(T):
    W = list(input())
    K = int(input())

    wg2 = WordGame2(W=W)

    result = wg2.game(k=K)

    for r in result:
        print(r, end=' ')