M = int(input())
    

def add(sets: set, value: int):
    sets.add(value)

def remove(sets: set, value: int):
    sets.remove(value)

def check(sets: set, value: int):
    if value in sets:
        return 1
    else:
        return 0

def toggle(sets: set, value: int):
    if value in sets:
        sets.remove(value)
    else:
        sets.add(value)

def all():
    return set(i for i in range(1, 21))

def empty():
    return set()

sets = set([])
for _ in range(M):
    command, value = map(str, input().split())

    if command == "add":
        add(sets, value)
    if command == "remove":
        remove(sets, value)
    if command == "check":
        print(check(sets, value))
    if command == "toggle":
        toggle(sets, value)
    if command == "all":
        sets = all()
    if command == "empty":
        sets = empty()


