import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

class Queue:
    queue = deque([])

    def push(self, number: int):
        self.queue.append(number)
    
    def pop(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue.popleft()

    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def back(self):
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[-1]

for _ in range(N):
    queue = Queue()
    command = input().strip()

    if 'push' in command:
        _, value = command.split(' ')
        queue.push(value)
    elif 'front' == command:
        print(queue.front())
    elif 'back' == command:
        print(queue.back())
    elif 'size' == command:
        print(queue.size())
    elif 'empty' == command:
        print(queue.empty())
    elif 'pop' == command:
        print(queue.pop())
