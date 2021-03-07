import sys
input = sys.stdin.readline

def rightOne(n):
    return (n*10) + 1

def mulTwo(n):
    return n * 2

def bfs():
    queue = [(A, 1)]

    while queue:
        a, c = queue.pop(0)
        if a == B:
            return c
        add = rightOne(a)
        mul = mulTwo(a)
        if add == B or mul == B:
            return c + 1
        if add < B:
            queue.append((add, c+1))
        if mul < B:
            queue.append((mul, c+1))
    return -1

if __name__ == "__main__":
    A, B = map(int, input().split())
    print(bfs())